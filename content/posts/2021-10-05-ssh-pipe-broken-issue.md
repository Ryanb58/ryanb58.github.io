title = "SSH Broken Pipe Issue"
date = 2021-10-05T17:47:00+02:00
tags = [
    "ssh",
    "disconnect",
    "broken",
    "pipe"
]
published = true
+++++

## Problem:

My laptop struggles at keeping an SSH connection alive with its default settings. See my pipe break below.

```
ubuntu@ip-10-106-2-194:~$ client_loop: send disconnect: Broken pipe
```

This is very annoying, especially if you are attempting something that requires long intervals of inactivity between commands.

## Solution:

Glancing through the SSH documentation, I found two settings that looked to be of importance. 

 - ServerAliveInterval
 - ClientAliveInterval

They appear to be intervals that can be set on the server or client that send a keep alive request through the connection.

By setting the `ServerAliveInterval` on my local machine I found my SSH connections to persist without intervention. 

File: ~/.ssh/config:

```
ServerAliveInterval 120
```

I also went ahead and put the `ClientAliveInterval` setting into my personal AWS boxes.

File: /etc/ssh/sshd_config
```
ClientAliveInterval 120
```

Enjoy!

#### Sources:
[https://man.openbsd.org/ssh_config#ServerAliveInterval](https://man.openbsd.org/ssh_config#ServerAliveInterval)
[https://man.openbsd.org/sshd_config#ClientAliveInterval](https://man.openbsd.org/sshd_config#ClientAliveInterval)