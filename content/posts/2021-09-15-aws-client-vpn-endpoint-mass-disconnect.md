title = "Moving an AWS Site-to-Site VPN to Another VPC"
date = 2021-09-01T17:47:00+02:00
tags = [
    "disk",
    "cleanup",
    "linux",
    "freespace"
]
published = false
+++++


Today, I experienced quite the panic attack. Everyone lost access to our externally setup VPN to our AWS subnet.

Error in TunnelBlick:

```
2021-09-15 14:25:13.798239 VERIFY OK: depth=0, CN=aws-client-vpn-clear.clearui.com
2021-09-15 14:26:13.435099 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
2021-09-15 14:26:13.435885 TLS Error: TLS handshake failed
2021-09-15 14:26:13.436066 SIGUSR1[soft,tls-error] received, process restarting
```

the CRL expired.. had to issue a new one..

#### How to Issue a new CRL!