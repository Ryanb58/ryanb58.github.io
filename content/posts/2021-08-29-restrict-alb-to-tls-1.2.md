title = "How to Restrict an AWS Application Load Balancer to TLS 1.2"
date = 2021-08-28T17:47:00+02:00
tags = [
    "aws",
    "alb",
    "tls",
    "encryption"
]
published = true
+++++

This weekend, I restricted the use of TLS to 1.2 and higher. Figure I'd document it a bit here.

1) Navigate to the Load Balancers page(under VPCs)
2) Select the ALB you want to update.
3) Click on the `Listeners` tab.
4) Select the HTTPS listener.
5) Click edit.
6) Change the security policy to `ELBSecurityPolicy-FS-1-2-Res-2020-10` or something more up to date.
7) Click the `Update` button in the top right.

Here is a list of the different types of security policies that you can enable via AWS.

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)

Hopefully, you don't have to do these updates manually, but it still helps to know how. Use IaC, it helps a ton in the long run.

Enjoy!
