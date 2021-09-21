title = "Most Important SCP Commands"
date = 2021-09-21T17:47:00+02:00
tags = [
    "network",
    "transfer",
    "linux",
    "scp"
]
published = true
+++++

SCP is a command that allows you to copy files and directories securely between two hosts. 

## Upload a file from local to remote host.

```
scp -i ~/.ssh/id_rsa client.rpm ubuntu@10.x.x.100:/remote/directory
```


## Upload a directory from local to remote host.

```
scp -i ~/.ssh/id_rsa -r /home/user/documents ubuntu@10.x.x.100:/remote/directory
```

## Download a file from a remote machine.

```
scp ubuntu@10.x.x.100:/remote/client.rpm /local/directory
```

Enjoy!