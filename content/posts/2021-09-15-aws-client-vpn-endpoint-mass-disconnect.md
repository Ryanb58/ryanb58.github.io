title = "AWS Client VPN Endpoint Mass Disconnect"
date = 2021-09-29T17:47:00+02:00
tags = [
    "aws",
    "disconnect",
    "vpn",
    "endpoint",
    "aws",
    "certificate",
    "revocation",
    "list",
    "crl"
]
published = true
+++++


### Problem:

A scary thing happened recently. Everyone at work lost access to our companies VPN. All of our applications run within an internal network hosted on AWS and most of my coworkers need to connect in order to do their jobs. Sadly, this VPN was setup by a previous employee who didn't document anything.

### Solving It:

Immediately I checked my own connection TunnelBlick and found the following exception:

```
2021-09-15 14:25:13.798239 VERIFY OK: depth=0, CN=aws-client-vpn-clear.clearui.com
2021-09-15 14:26:13.435099 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
2021-09-15 14:26:13.435885 TLS Error: TLS handshake failed
2021-09-15 14:26:13.436066 SIGUSR1[soft,tls-error] received, process restarting
```

Looks like there was an issue with the handshake for our TLS encryption... or so I thought. Ends up this is a side effect of our Certificate Revocation List expiring!

### What is a Certificate Revocation List(CRL)?

A CRL is a list of certificates that are revoked before their expiration date.

For example, each individual employee at a company has a certificate that grants them access to the companies cloud servers. One day, a coworker decides to quit. If their certificate is still valid then they can continue to login to the companies servers and possibly abuse that access if their certificate has not yet expired. To address this, we add their certificate to a list that prevent them from accessing your companies servers anymore. Then when their cert expires, it will be removed from the CRL as it posses no more threat.

### How to Issue a new CRL!

1. Clone the following tool: [Easy-RSA](https://github.com/OpenVPN/easy-rsa/).
2. Navigate into the repo and into its `easyrsa3` sub folder.
3. Generate a new CRL.
```
./easyrsa gen-crl
```

4. Navigate to VPC > Client VPN Endpoint.
5. Select the endpoint that stopped working.
6. Choose Actions > Import Client Certificate CRL.
7. Copy over your CRL file you generated in step 3 and submit.

Once the steps above are completed, you should be able to connect to your VPN Endpoint again.

Enjoy!

Update: Looks like AWS already has this process documented:
[https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html)
