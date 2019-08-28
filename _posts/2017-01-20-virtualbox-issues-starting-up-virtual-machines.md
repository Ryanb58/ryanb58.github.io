---
title: "VirtualBox Would Not Start My Virtual Machines."
date: 2017-01-20T23:49:57-05:00
---

Murph's Law - "Anything that can go wrong will go wrong."
Source - https://en.wikiquote.org/wiki/Murphy's_law


Virtualbox Log:
00:00:00.387310 Audio: Initializing PulseAudio driver

Virtualbox would be stuck trying to initalize my VM.

Ran through everything possible. Uninstalled Virtualbox, Re-installed Virtualbox, Re-installed different versions of virtualbox, checked kernal modules. etc..

Ran the purge command:

```
sudo apt-get remove virtualbox* --purge
```

Ended up going into the settings of each virtual machine and disabling the pulse audio audio driver.

