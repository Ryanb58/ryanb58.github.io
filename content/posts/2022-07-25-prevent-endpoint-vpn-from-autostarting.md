title = "Autostart Dark Pattern - Endpoint Security VPN for Mac"
date = 2022-07-25T17:47:00+02:00
tags = [
    "mac",
    "annoyance",
    "autostart",
    "startup",
    "prevent",
    "endpoint",
    "security",
    "vpn"
]
published = true
+++++

Ethically, every program that has autostart capabilities should have an **easy to access** setting that allows its users to prevent that behavior. Sadly this isn't the case with all software. 

For example, I have been working with a client in my 9to5 that uses a software called "Endpoint Security VPN" by Checkpoint which does not provide autostart as an easily configurable setting. Luckily I have a easy solution.

First open up your terminal.

Copy & Paste the following command into your terminal to change it's hidden "autostart" setting. 

```
sudo plutil -replace RunAtLoad -bool NO /Library/LaunchAgents/com.checkpoint.eps.gui.plist
```

Kill the program so the changes take affect.

```
pkill -f "Endpoint Security VPN"
```

Enjoy your reduced boot time! 
