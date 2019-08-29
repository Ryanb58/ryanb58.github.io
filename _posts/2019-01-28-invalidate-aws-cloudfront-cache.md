---
title: "Invalidate AWS CloudFront Cache"
date: 2019-01-28T15:51:58-05:00
tags:
  - aws
  - cloudfront
---

Today, I needed to invalidate a specific Distribution's cache on AWS Cloudfront.
This resulted in me searching through the AWS cli tool's docs.
Luckily I was able to uncover a command to accomplish such a task.

```
aws cloudfront create-invalidation --distribution-id DISTRIBUTION_ID --paths /\*
```

Simply replace **DISTRIBUTION_ID** with the proper ID and you will be good to go.