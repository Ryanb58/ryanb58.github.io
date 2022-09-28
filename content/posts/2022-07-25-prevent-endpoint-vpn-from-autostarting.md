title = "Autostart Dark Pattern - Endpoint Security VPN for Mac"
date = 2022-07-25T17:47:00+02:00
updated = 2022-09-28T17:47:00+02:00
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

## UPDATE: 2022/09/28

Recently the app began to autostart again. After some researching, I found a [stackoverflow comment](https://superuser.com/a/1370652) about another settings file, a setting called `KeepAlive`, and some more **autostart** files. The command below allows you to turn off the extra settings.

```
sudo plutil -replace KeepAlive -bool NO /Library/LaunchAgents/com.checkpoint.eps.gui.plist
sudo plutil -replace RunAtLoad -bool NO /Library/LaunchDaemons/com.checkpoint.epc.service.plist
sudo plutil -replace KeepAlive -bool NO /Library/LaunchDaemons/com.checkpoint.epc.service.plist
```

Then delete the checkpoint security "autostart" files for your user.
```
sudo rm -f /Users/${USER}/Library/LaunchAgents/net.pulsesecure.*
```

## Original Post:

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
make 