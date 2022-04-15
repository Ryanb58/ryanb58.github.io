title = "How To Prevent Mac From Auto Switching Desktops"
date = 2022-04-15T17:47:00+02:00
tags = [
    "mac",
    "annoyance",
    "bug",
    "fix"
]
published = true
+++++

During my time using a mac, I have run into an annoying issue where the Desktop switcher seem to want me to organize things by application instead of by project. This would lead to frustrations such as when selecting a new desktop, it auto-switching back to the desktop I was previously on.

Today, I decided to google it. Low and behold I came across [jgl777](https://discussions.apple.com/thread/4995042?answerId=21918357022#21918357022) who had the answer.

Open a terminal and perform the following commands:
```
defaults write com.apple.dock workspaces-auto-swoosh -bool NO
killall Dock
```

Enjoy your working, NON auto switching mac. 

Sources:
https://discussions.apple.com/thread/4995042
