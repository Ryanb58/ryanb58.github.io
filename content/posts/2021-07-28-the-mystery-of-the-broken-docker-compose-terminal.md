title = "The Mystery Of The Broken Docker Compose Terminal"
date = 2021-07-28T17:47:00+02:00
tags = [
    "incident",
    "terminal",
    "prompt",
    "docker",
    "compose"
]
published = true
+++++

I have been highly annoyed over the last few weeks with my docker containers terminal prompts. It would mess up everytime I'd try to use tab complete, up/down arrows, or copy/paste. The screne would display weird characters and sometimes just not respond.

Command I use to get a shell inside of a new container:

```
docker-compose run --service-ports app /bin/bash
```

Then when I try to use my arrow up/down keys I get the following:

```
root@81918ad1f93a:/data/web# ^[[A^[[A^[[A^[[A
```

This highly impeded my ability to get work done.

#### Solution:

Ends up the issue is with `docker-compose` version  `v2.0.0-beta.6` which must have some bugs because it has been making my terminal go haywire.

You can check your version with the following commands:

```
docker-compose version
docker compose version
```

I fixed the issue by getting off of the experimental version using these instructions:

Click the docker icon on the top menu bar. Select `Perferences`>`Experimental Features` and uncheck `Use Docker Compose V2`. I then restarted docker and everything was back to normal with my `docker-compose` alias pointed back at version `version 1.29.2`.


