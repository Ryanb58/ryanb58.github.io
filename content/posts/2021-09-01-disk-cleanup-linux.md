title = "Disk Space Clean Up on Linux"
date = 2021-09-01T17:47:00+02:00
tags = [
    "disk",
    "cleanup",
    "linux",
    "freespace"
]
published = true
+++++

Every now and then one of my legacy sites goes down due to having a full disk. This kind of stinks and I should automate a solution. But until then, I figure I'd document all the ways I've gone about "cleaning" them up.

    Note: These suggestions are in no particular order.


First you should know how to check your total disk usage. The following command does just that. It gives you a birds eye view of your entire system in human readable form.

```
df -h
```

#### Check Journal disk usage.

```
journalctl --disk-usage
```

This one always gets me. I seem to keep way more logs than I need. Use the following command to cleanup logs older than 14 days.

```
sudo journalctl --vacuum-time=14d
```

#### Get rid of unused packages.

This one is great for old systems, as they have probably been through an upgrade or two. Running the following command removes packages that were installed to satisfy dependencies. Sometimes those packages get removed but their dependencies dangle.

```
sudo apt-get autoremove
```

#### Clean up your APT cache

APT keeps an cache of previously installed packages, even after they have been uninstalled. First check how much space those are using.

```
sudo du -sh /var/cache/apt 
```

Then clean it up.

```
sudo apt-get clean
```

Enjoy!