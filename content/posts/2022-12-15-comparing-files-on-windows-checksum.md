title = "Comparing Files(Checksum) On Windows"
date = 2022-12-15T06:47:00+02:00
tags = [
    "microsoft",
    "windows",
    "checksum",
    "compare",
    "files",
    "hash",
    "powershell",
    "linux"
]
published = true
+++++

Recently, I needed to compare two DLLs with the same name to see if they were the same. However, my existing Unix knowledge was useless as I do not have the Ubuntu subsystem installed.

So I did what any engineer in my position would do, I asked my more experienced peers. 

A Principal Engineer @ work gave me some guidance. They introduced me to a PowerShell utility named [Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.3) which was exactly what I was looking for.

In my scenario a user had a version of a .DLL installed on their machine of which I needed to ensure was a specific version. Knowing about `Get-FileHash` allows me to ask the customer to perform the following command and message us the results.

```
PS > Get-FileHash .\sapnco.dll

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          E79E3BC34494C5F9102FBFA61AED2B2177A58CB0DE16B812AD0AAF9B6BA3261F       C:\...\sapnco.dll
```

Then I went ahead and performed the command on my own machine and verified the hashes matched.

#### Extra TidBit - Checksum On Linux

```
ubuntu@ip-x-x-x-x:~/app$ sha1sum docker-compose.yml
2571e3153b90517693c2dfc5668746296023ccda  docker-compose.yml
```

Enjoy!