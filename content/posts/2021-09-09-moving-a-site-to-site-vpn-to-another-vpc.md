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

Today I found myself in quite the predicament. One of my sub VPC's private Ip address space clashed with another sub VPC. The simple solution is just to recreate them using the terraform scripts I have built out. However, one issue still remains... Each VPC is connected to a customers network via a Site-to-Site VPN. These VPNs took weeks to get setup between figuring out who to talk to and what firewall requests I had to make, thus redoing their VPNs was not possible. 

## TLDR:

1. Create a new VPC in non-clashing IP private space using my terraform scripts.
2. Disconnect the Site-to-Site VPN from the existing VPC.
3. Attach the Site-to-Site VPN to the new VPC.
4. Reach out to the customer and ask them to update their routes.

