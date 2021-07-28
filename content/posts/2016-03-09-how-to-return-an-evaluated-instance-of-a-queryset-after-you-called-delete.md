title = "How To Return An Evaluated Instance Of A QuerySet After You Called Delete"
date = 2016-03-09T17:47:00+02:00
tags = [
    "django",
    "evaluate",
    "solution",
    "memory"
]
published = true
+++++

### Problem:

We have a Django rest framework endpoint that lists out tasks that are being processed, each task includes its relative status. Say a task is in progress, it would report as &#8220;In Progress&#8221; then when it is completed by our back-end workers, the task reports as &#8220;Successful&#8221; and will continue to exist in our database, and there lies the problem. As more and more tasks are added to our system, we continue to have to increase our capacity for the table in our database that holds these task records.

### Solution:

Load the QuerySet object, force Django to evaluate it into memory, then call the delete query on the actual database. Last but not least, return the data that was evaluated into memory.

#### Code:

```
# List forces evaluation of query set so data is now in memory.
tasks = list(Task.objects.all())

# Have Django delete the successful tasks from the database,
# but not from memory.
Task.objects.all().filter(status="Successful").delete()

# Return the tasks in memory.
return tasks
```

Enjoy!