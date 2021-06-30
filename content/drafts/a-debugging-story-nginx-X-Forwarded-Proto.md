Sometimes you come across something that isn't crazy interesting, but has value nevertheless. This is one of those posts.

While woring my day to day, after a meeting, our CEO mentioned in pass that pagination wasn't working for one of our customers. Initially this doesn't seem like it would be that big of an issue, however, it manifested itself in one of the worst places; our audits page. 

This Audits page is used quite a lot by our services team, as it's essentially their rendition of version control. Meanwhile, my entire job's existance relies on making the service team happy. Thus the journey begins. 

The first step was to reach out to my boss to keep him informed. We both jumped on a call and talked it over. He even moved forward with some pair debugging since he had the time.

This involved testing the bug on our dev instance, not being able to reproduce it, then moving on to test it on specific customer's dev box. We happily were able to reproduced the issue in the customers dev instance. This lead us to thinking about our recent code changes. We poked through them and decided that none of the most recent changes had even come close to touching this code, so we moved on. 

Next, we opened the Chrome Inspector on the page and looked at the response we got from our call to the paginated API endpoint. This brought us somewhere interesting. On the networking tab, in the Status portion of the network request we saw `(blocked:mixed-content)`. Eureka! 

The issue was obviously an HTTP call on an HTTPS page. But why? 

First, some context. The customers instance that we were looking at is a dockerized version of our application. Our dev instance and the majority of our other customers have not been through this transition yet. This was known, but they had been successfully using our app for months now, so that initially seem like it would be the problem. 

However, along with the dockerization of our applicaiton we determined that HTTPS termination should not be handled by our own nginx proxy. Instead we wanted to offload this to our AWS ALB. By doing so we gain a few benefits.. one of the most important to us, currently, is not having to deal with our certs expiring. Instead AWS can rotate the certs on our behalf.

So we dove deep into our React frontend and found that the amazing developer who wrote the code uses the URL for `next` provided by the API. Good design for sure, but something was wrong. Ends up the API was returning hyperlinks with a prefix `http://` instead of what we expected `https://`. 

Our application's API is provided by Django Rest Framework(DRF) which is built on-top of Django. However, as I browsed their documentation, I didn't notice anything that identified how `https://` was set. Back in our codebase, I identified a `DEFAULT_PAGINATION_CLASS` of  `rest_framework.pagination.LimitOffsetPagination`. So into the source code we go. 

Once I find the source on github, I set the library version via the tags, and `CTRL + F`ed for `class LimitOffsetPagination`. This brought me exactly where I wanted to go. I see a method called `get_paginated_response` which looks to return a dictionary with the `next` URL. I then follow the rabit hole a bit more and look at the `get_next_link` method. It is here that I see the following line:

```
url = self.request.build_absolute_uri()
```

I make the assumption that self.request is a Django Request object and start using my Googlefue. 

I instantly come across the main Django docs and as expected; `build_absolute_uri` builds a uri. Time to dive into more source code.

https://github.com/django/django/blob/8bcb00858e0ddec79cc96669c238d29c30d7effb/django/http/request.py#L183

As you can see on line 216, the URL is constructed from `self._current_scheme_host` abd `self.path`. I only care about the first part. 

`_current_scheme_host` looks to be a method used for caching. It combined `self.scheme` and `self.get_host`. 

I scan through the class and find `self.scheme` being set via `@property`. IT"S A METHOD! Set by a django setting of `SECURE_PROXY_SSL_HEADER`. So off we go back into our code base to see what's up. 

The following config file line looks fine..

```
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
```

So what is happening? Time to dive into the weeds even more. Lets see how requests are getting to our application. Ah ha, that hecking nginx stuff. That's what handles requests. 

```
server {
    listen 80;
    charset utf-8;

    ...

    location / {
        ...
        proxy_set_header X-Forwarded-Proto $scheme;
        ...
    }
}
```

See what I see? The `X-Forwarded-Proto` header is being set to $scheme. Time to look up more docs!

https://nginx.org/en/docs/http/ngx_http_core_module.html#var_scheme

Seems that `scheme` is exactly what we are looking for. Depending on what this is set to, django will interpret that as what protocol the client ended up connecting with.

Proxy Visualization:

Customer <-> AWS ALB <-> Nginx <-> Django App

So the issue comes down to AWS ALB doing our HTTPS termination and our Nginx instance not passing through the `X-Forwarded-Proto` header, but instead rewriting it to be the protocol used by the request between the AWS ALB and itself. Once quick line change and we are good to go.

```
-proxy_set_header X-Forwarded-Proto $scheme;
+proxy_pass_header X-Forwarded-Proto;
```

Bam! All that work for a one line change. Just another example of how complicated debugging can be. Remember to try to not interupt your engineers when they are in the middle of something like this. Having to make that context switch can be down right dreadful.
