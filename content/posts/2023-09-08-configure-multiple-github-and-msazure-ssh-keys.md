title = "How to Configure Multiple SSH Keys for GitHub and Azure DevOps Repos"
date = 2023-09-08T06:47:00+02:00
tags = [
    "github",
    "msazure",
    "azure",
	"devops",
	"ssh",
	"keys",
	"authentication",
	"multiple",
	"manage"
]
published = true
+++++

Recently, I've encountered situations where I need to work with multiple git repositories from different sources. This often includes interfacing with repositories on both GitHub and Azure DevOps. Without the proper setup, I encounter generic errors in git, especially when trying to clone new repositories.

I primarily use SSH keys to manage authentication with these services. To streamline the process, it's useful to configure the `~/.ssh/config` file to point each host to the appropriate key. Below is an example that you can use for your own configuration.

```shell
Host github.com
	AddKeysToAgent yes
	UseKeychain yes # mac only
	IdentityFile ~/.ssh/github
	HostName github.com

Host bitbucket.org
	AddKeysToAgent yes
	UseKeychain yes # mac only
	IdentityFile ~/.ssh/bitbucket
	HostName bitbucket.org

Host vs-ssh.visualstudio.com
	AddKeysToAgent yes
	UseKeychain yes # mac only
	IdentityFile ~/.ssh/your-azure-devops
	HostName vs-ssh.visualstudio.com
	IdentitiesOnly yes
	PubkeyAcceptedAlgorithms +ssh-rsa
	HostkeyAlgorithms +ssh-rsa
	Host ssh.dev.azure.com

HostName ssh.dev.azure.com
	User git
	AddKeysToAgent yes
	UseKeychain yes # mac only
	IdentityFile ~/.ssh/your-azure-devops
	IdentitiesOnly yes
	PubkeyAcceptedAlgorithms +ssh-rsa
	HostkeyAlgorithms +ssh-rsa
```

Enjoy!