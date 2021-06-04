title = "Leaning Towards Terraform"
date = 2021-06-03T00:00:00+02:00
tags = [
    "devops",
    "aws",
    "cloudformation",
    "terraform",
    "infastructure",
    "provision",
    "iac"
]
+++++

As life progresses, I grow closer and closer to the machines that run my code. This leaves me with a sour taste though, because accountabilty in terms of infastructure changes can be lacking. In turn, I have been expected to know more about the interworkings of the cloud infastructures which we are using. In this post I'd like to analyze some reasons I might switch away from AWS CloudFormation and turn my attention towards Terraform.


1. Updating a Security Group

The first issue I ran into is changing the description on a security group. This should be an update, but ended up being a delete then create. Not what I was expected. Luckily my customer wasn't yet using the site, so there was no bad experience, unlike the guy in this blog post: [Security Rule Gotchas](https://jlordiales.me/posts/2018/01/aws-cloudformation-gotchas-security-groups/)


2. Separation of the planning vs execution state.

Knowing what changes are going to be performed before making them is a game changer; especially when working with a team of people. Seeing the changes that are about to be made allows for better planning and better change reviews. Sadly, this is something that is lacking in CloudFormation.


3. Modularity

Terraform allows you to use 3rd party modules to integrate with services beyond just your single cloud provider. Say for example, business has determined that the risk of all their tech only using AWS has grown to big. So they task you with seting up your application in a hybrid cloud approach. This is impossible if you only use CloudFormation, but with Terraform its no big deal. Sure there will be some sleepless nights as deadlines approach, but at least you can make changes and work within the boundries that have already been established.


4. Limits

Did you know that Cloudformation Templates have a size limit? Yep, 51,000 bytes. Also a resource limit, 200 items. Givin, those are pretty high limits. However, if you have ever inherited a jumbled mess of infascture code that is all in one file. It's almost enough paint to make you physically cry when you have to add one more resource, you hit the limit, and business yells because deadlines. Sometimes there just isn't enough time to refactor that large mess.


5. Existing Resources 

A lot of the startups I have worked for tend to start from scratch. They do things in a manual way in the Cloud until their scale gets big enough to add a Operations person to the mix. Adding existing resources seems to be quite easy in terraform. You simply run a command:

```
terraform import aws_security_group.elb_sg sg-903004f8
```

meanwhile in cloudformation there seems to be a lot of confusion on how to do this, and if it is [even supported](https://stackoverflow.com/questions/54427486/incorporate-existing-aws-resources-into-a-cloudformation-stack):



Sources:
https://www.missioncloud.com/blog/aws-cloudformation-vs-terraform-which-one-should-you-choose
https://www.terraform.io/intro/vs/cloudformation.html
https://medium.com/@endofcake/terraform-vs-cloudformation-1d9716122623
https://blog.gruntwork.io/why-we-use-terraform-and-not-chef-puppet-ansible-saltstack-or-cloudformation-7989dad2865c#.63ls7fpkq
https://medium.com/@cep21/after-using-both-i-regretted-switching-from-terraform-to-cloudformation-8a6b043ad97a
https://binx.io/blog/2019/06/14/nine-reasons-to-use-cloudformation-instead-of-terraform/
https://stackoverflow.com/questions/54427486/incorporate-existing-aws-resources-into-a-cloudformation-stack
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group#import
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html

