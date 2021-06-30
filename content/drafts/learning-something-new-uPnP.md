

Today I am learning something new. 

I came across a blog post by [Kevin Norman](https://kn100.me/turning-upnp-off/) who talks about how his NAS punched its way through the local consumer router, exposing itself to the world. This sparked my attention, as how could it even do such a thing without human input? From what I remember with my time at the local career , you had to manually forward ports to allow a local website to be accessible from the public web. Ends up this isn't the case anymore with a technology called uPnP. 

uPnP stands for Universal Plug and Play. It is a set of networking protocols built on top of TCP/IP stack. According to uPnP-hacks.com it was created back in the 1990s by Microsoft as a competiting protocol to Sun's JINI. The main reason for it's development was to allow networking devices to attach themselvs to networks in comparison to how a hot swappable harddrive can be added to your NAS box. 

Some interesting use cases:

- Discover an xBox on the network.
- Allow your IP Webcam to be publically accessible.
- Retrieve music and video from a media server.
- Allow smarthome appliances to discover each other and share info.
- Enable syncing of local IoT devices

While going down this rabbit hole of discovery I came across one of my own favorite project uses uPnP for local disovery. WLED. Neat hu? 

Sources:
https://en.wikipedia.org/wiki/Universal_Plug_and_Play
http://www.upnp-hacks.org/upnp.html