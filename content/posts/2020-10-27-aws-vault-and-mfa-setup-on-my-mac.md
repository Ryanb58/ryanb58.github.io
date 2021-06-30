title = "AWS Vault and MFA Setup on my Mac"
date = 2020-07-21T17:47:00+02:00
tags = [
    "mfa",
    "aws",
    "vault",
    "mac"
]
published = true
+++++

Recently, I decided to secure my local machine by downloading and using AWS Vault. To my surprise, setting up MFA with Vault required a step or two more that I wasn't expecting. Here are my findings/steps. 

First, I used homebrew to install aws-vault.

```
brew cask install aws-vault
```

Then I added my profile and followed the instructions which had me provide my Access ID and Secret.

```
aws-vault add taylor
```

Then I tried to list out the S3 buckets via:

```
aws-vault exec taylor -- aws s3 ls
```

This resulted in the following error.

```
An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied
```

So I opened up my AWS config file in Visual Studio Code.

```
code ~/.aws/config
```

Doing so lead me to see that my profile didn't have a `mfa_serial` variable defined. I found my key in IAM under my own user's Security Credentials tab and added it to the file.

Now, my config file had the following in it: 
```
[profile taylor]
mfa_serial=arn:aws:iam::XXXXXXXXXX:mfa/taylor
```

And when I performed my s3 listing again, it worked.

Originally Posted on [dev.to](https://dev.to/mrbrazel/aws-vault-and-mfa-setup-on-my-mac-37dk)
