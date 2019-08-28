---
title: "FAQ - Service Oriented Architecture for a Small Team"
date: 2019-01-17T10:30:56-05:00
draft: true
toc: false
images:
tags:
  - service
  - SOA
  - architecture
  - small
  - team
  - kubernetes
  - containers
  - docker
---

FAQ about going towards a SOA with a small team(3 to 6 people).

#### Are you experiencing any of the following pain points?
 - Hard to scale your current app.
 - You are taking on coders who know different languages.
 - Your developers want an over simplified solution.
 - Your entire application crashes whenever an error occurs.
 - Do you have a piece of your application that consumes more of one type of resource than the others?(CPU, RAM, GPU, etc...)
 - Developers depending another developers work to get their own work done?
 - Can't deploy a release during high peak traffic times.
 - Are using docker for local development, but hosting on good o'bare metal or EC2 boxes with no sight of a containerized prod in the works.

Then micro-services is probably the right path for you.

#### How do you manage the services?

Small team - Use a managed Kubernetes cluster(EKS, GKE, AKE, etc...)



#### How do you debug a problem?

#### Can you scale the system easily?

#### What do you do about logging?

Con:

Overhead of tooling
Overhead of getting it setup in practice.


