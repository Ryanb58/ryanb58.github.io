---
title: "Performance Problems in your Node.JS App"
date: 2018-11-19T23:49:57-05:00
---

Recently, I have inherited a Node backend that was written with a lot of
constraints and little planning in mind. The person working on the code before
me claimed to be an "expert" in writing javascript for the backend, however
at the end of the day it all comes down to experience and understanding.

The code was slow, no denying that. The people before me took steps to help
speed the application up. A few of those steps were things like looking at the
slow SQL queries and moving that code back into node, setting up
[throng](https://github.com/hunterloftis/throng) to run multiple "workers" on
the same server, and added autoscaling into the mix so that the application
could be scaled horizontally when a threshold was met.

So now it is up to my buddy Gerrit and I. We are the last leg of defence.

First we need to layout how problems are really solved.

1) Identify the problem.
2) Get baseline data that we want to beat.
3) Define solutions
4) Implement a solution.
5) Reuse the test we used for the baseline. Do results beat the baseline?
   - If not then restart at step 3.
6) Success!

#### Identify The Problem

First I was under the impression that Node worked similar to how python works.
That was a huge and misleading assumption. Because of this Gerrit and I spent a
 hefty amount of time working on building unittests for the top 5 slowest
 endpoints. My goal was to write each unittest then come back and profile them
 individually. Whereas in python I would be able to get a clean stack trace
 and identify where in the code the app was spending the majority of it's time,
 this proved to be much more difficult in Node.

I tested out






1) Unittests
 - Profiling the application like I would do in python.

2) Blocker + Locust.

Where too from here?

3) Kue?

Decided it might not be the best route.
 Performance
 Seeing into failures.
 etc.

4) Nope, going with Bull.

https://www.reddit.com/r/node/comments/4m6cjd/kue_is_super_unreliable_any_alternatives_for/

https://news.ycombinator.com/item?id=17473511

https://medium.com/one-more-thing-studio/procrastination-like-a-boss-with-queues-db65b9130776
