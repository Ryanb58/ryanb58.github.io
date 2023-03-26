title = "Log Rotation For Docker Containers"
date = 2023-03-26T06:47:00+02:00
tags = [
    "docker",
    "container",
    "log",
    "rotation",
    "logging",
    "fluentd",
    "splunk"
]
published = true
+++++

One of the twelve pillars of a well behaved application is "Logs". However, having an infinitely expanding file on your server isn't ideal. So let's rotate it.

Logging parameters.

Docker allows you to configure two parameters. `max-size` and `max-file`. 

`max-size` specifies how big a single file can be. So one container can have a log size as big as X megabytes.

`max-file` is the maximum number of log files persisted at any given time. 

To change these we simply have to create or edit a daemon settings file.

```
sudo vim /etc/docker/daemon.json
```

and update it's contents to match the following.

```json
{
	"log-opts": {
		"max-size": "128m",
		"max-file": "128"
	}
}
```

The combination above allows for up to 128 128MB files at once for a total of 16.38400 gigabytes of used storage at max capacity.

For the change to take effect you'll also need to restart the daemon & all of your containers.

```
sudo service docker restart
```

	Pro Tip: Use fluentd & splunk to transform and aggregate your logs to a centralized location.

Sources:
[12 Factor](https://12factor.net/)
[Docker Documentation](https://docs.docker.com/config/containers/logging/configure/)