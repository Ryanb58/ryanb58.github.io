
title = "Django Migrations Downgrade in Docker Swarm"
date = 2018-03-02T17:47:00+02:00
tags = [
    "docker",
    "django",
    "python",
    "downgrade",
    "swarm",
    "orchestration"
]
published = true
+++++

Edge cases are a big problem in software engineering, one that I recently ran
into while on a beta box was errors being thrown after a downgrade.

First a little background on the application. It is a django application running
in a docker container via docker-swarm. Our application upgrade/downgrade
process is to reduce the amount of containers running down to 0. Change the
tag numbers in our .yml file and then scale them back up. This forces the
containers to download the newly defined version. Note that our downgrade
process is exactly the same we just update the a tag with an older version.

The process described above might sound correct to you, however, because we use migrations
to structure our database the process is flawed. By replaceing the tag and
just moving to older docker containers, the downgrade function inside our
migrations never get ran. Instead the downgraded application has no idea
about the migrations that existed in the newer version that does not in it's
own. Thus resulting in an inconsistant database state with the version of
application deployed.

My current solution to this issue is to run the migration downgrade for each
app in our django project manually inside of the existing application container
. To do this I start out with a diff of the code between the old version and
the new version. I look for any added migrations and run the command below to
have django south run through the downgrade methods until it reaches the
latest migration in the old code. Then I perform the old migration method.

Here is a step by step list of the process.

1) Diff of code.

2) Write down oldest added migration number and app name

3) Exec into the application docker container.

4) Migrate backwards :

```
./manage.py migrate appname 0000
```

5) Exit out of container.

6) Scale the swarm down to 0 nodes.

7) Change tag number.

8) Scale the containers back up.


Do you have any suggestions or any improvements to this process? Comment below
and link me to other articles you've read about this process. The more we know
together the better our overall solutions can be.