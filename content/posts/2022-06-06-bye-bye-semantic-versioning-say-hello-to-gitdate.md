title = "Bye Bye Semantic Versioning, Say Hello To GitDate"
date = 2022-06-06T17:47:00+02:00
tags = [
    "my",
    "versioning",
    "system",
    "gitdate"
]
published = true
+++++

## Quick Rant About Semantic Versioning

There is inherit information loss when a developer implements Semantic Versioning.
Taken back a little by that statement? Well, let's ask if it's true?

- When was the last time you could tell someone the difference between version 1.2.1 and 1.2.3 quickly?
- Can you tell me when version 1.2.1 was released? Was it yesterday? Last year? Ten years ago?
- What is your company/team's meaning behind a major, minor, and patch increment?
- Who decides when a new major version is released? Is it a person? Maybe it's based on the size of an architectural change?
- What happens to the version where the manager or developer forgot to put together a change log?

Every developer I've come across so far knows about Semantic Versioning, but rarely do they have insight into the process at their companies. When I ask about the changes between version 1.2.1 and 1.2.3, I see them launch off on a new crusade, looking for their change logs.

This has been going on for years, and I think it's time for a new solution.

Over the past five years, I have been implementing what some might consider is heresy, but I see it as the future of versioning.

## Introducing, GitDate Versioning

The formula is simple:

```
year.month.day.git-short-code
```

Here are some examples:

- 2021.03.22.d31d336
- 2021.03.31.44cf59b1
- 2021.03.31.21df22d1
- 2021.05.25.5a2ac478
- 2022.02.14.2c52a964

#### Pros:
- Can tell the date the version was created.
- You can look up changes quickly by using git compare.
- Your infrastructure team gained visibility into when the software was last released.
- If the release process doesn't create a git tag, you can still clone a copy of the code for a specific version.
- The format can easily be extended.
- Customers now have visibility into the last time their software was updated.

#### Possible Cons:
- Multiple builds on the same day? You would need access to the git repo to figure out which came first.
- Customers now have visibility into the last time their software was updated.

If you have an opinion or suggestion, please leave it in the comments below.

Enjoy!