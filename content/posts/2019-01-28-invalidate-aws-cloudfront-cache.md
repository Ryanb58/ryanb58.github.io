title = "Invalidate AWS CloudFront Cache"
date = 2019-01-28T17:47:00+02:00
tags = [
    "aws",
    "cloudfront",
    "cache"
]
published = true
+++++

Today, I needed to invalidate a specific Distribution's cache on AWS CloudFront. This resulted in me searching through the AWS cli tool's docs. Luckily I was able to uncover a command to accomplish such a task.

```
aws cloudfront create-invalidation --distribution-id DISTRIBUTION_ID --paths /\*
```

Simply replace DISTRIBUTION_ID with the proper ID and you will be good to go.