---
title: "Hello World"
date: 2016-01-20T23:49:57-05:00
draft: true
toc: false
images:
tags:
  - virtual
  - machine
  - start
  - audio
  - pulse
---

Title: Writing Better Code
Date: 2016-09-015
Modified: 2016-09-26
Category: python
Tags: writing, better, code, refactoring, python, tips
Status: published


As a software engineer/artist I could spend copious amounts of time refactoring.
However, at some point products have to be shiped. You can't just keep
 pushing deadlines back further and further. Instead I utilize the tips below
 to provide functional code that is also clean.

## The DRY Principle.

DRY stands for "don't repeat yourself" and you shouldn't. If you do, STOP!
Repeating yourself will never be a good pratice.
The programming gods invented functions for a reason. Start now by splitting up
your big `main()` funciton.

## Design Patterns

What you might not of know is that there are three major categories of
design patterns; creational, structural, and behavioral. Each category having a
plethra of tools to help solve everyday software problems.

## Understand The Computer

Knowing that the windows registry exists and how to edit it is not "understanding"
the inner workings of a computer. Understanding a computer means having knowledge
about things such as the datapath on the CPU and different levels of cache.

If you don't understand how a CPU does computations such
as multiplication down at a binary level, how are you suppose to think in terms
of preformance? When your application is eating up precious cycles for useless
tasks, being able to optimize the program and utilizing your compilers internals
to elevate things to a kernel level commands can become of utmost importance.

## Tools

This one is really just based on how much experience a person has with the utilities
of their trade. Currently I use VS Code + a Vim Shortcut plugins. I then utilize
flake8 to keep my code style up to par and pylint to ensure no bugs exist in my
code.

I'm not saying switch to my tools, I'm saying start diving deep into how they work.
Ask yourself, are there any menu's or options you haven't explored before? Mess
around with them until you figure out. Can you use a tool in a way it wasn't meant to?
Try it. Don't settle, expand it and put it into your pipeline.

## Readability

This one is very important. Instead of writing a list comprehension that goes way past
the end of the 79 character PEP8 line length, use multiple lines. Name variables
approprately and keep packages clean. All things that you should be actively striving for
when writing code or refactoring.

## Code Reviews

Open source or not you should strive to get someone to review your code. This helps
promote a more open enviroment and prevents bugs from making it into production code.

## Testing

I could talk for hours on this one. Testing is essential.
Start out with unittests and verify small components of the system. Once
you get a hold of how to do that, start adding integration tests for business
essential parts of your application.

Have a ton of services? Test the main functionality of these programs by running
smoke tests. Smoke tests are very light weight scripts that verify the conditions
of your system. A good example of smoke tests is ensuring your FTP server is
online and that the user can login.

## Conclusion

Wrapping things up, you should always strive for clean and readable code. I hope
that some of the items I've listed above can enable you and your team to create
 amazing and beautiful products for people all over the world.

Please feel free to share this post and comment anything I left out or might be
able to improve on for my own sake.
