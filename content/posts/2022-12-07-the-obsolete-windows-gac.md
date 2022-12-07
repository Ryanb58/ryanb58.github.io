title = "The Obsolete Windows GAC"
date = 2022-12-07T06:47:00+02:00
tags = [
    "microsoft",
    "windows",
    "GAC",
    ".net",
    "shared",
    "code",
    "libraries",
    "global",
    "assembly",
    "cache"
]
published = true
+++++

While debugging an issue a customer reported issue, I became well acquainted with the Global Assembly Cache otherwise known as the GAC. In this post, I'll share my findings.

The GAC is a place where code is shared amongst multiple programs is stored & run. Quite an interesting concept and as the name implies it is a cache.

A key benefit of it being a cache is that only one instance of the code is ever loaded into memory. Therefore, if you have multiple programs using the same DLL, you don't have to worry about multiple instances of that DLL existing in memory at the same time. Keeping your RAM clean of non-duplicated code.

Another benefit to the GAC is the ability to have multiple versions of an assembly. When a library is updated, both versions 1.0 and 1.5 can sit alongside one another and your apps don't break. Programs that were referencing 1.0 can continue to do so, and newly added programs will reference the latest version 1.5. 

So why is the GAC obsolete?

1. The concept was removed from .NET 5 and later.
2. Memory has become less expensive. To the point where having duplicated code in memory is no longer a big issue.
3. It placed the responsibility of new version testing on the shared library developer.
4. Dangerous? Provides a good attack vector for hackers to inject code into existing programs.

For more information about the Windows Global Assembly Cache, please check out the sources linked below.

#### Sources:

https://learn.microsoft.com/en-us/dotnet/framework/app-domains/gac
https://learn.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/5.0/global-assembly-cache-apis-obsolete
https://stackoverflow.com/questions/538710/why-should-i-not-use-the-gac
http://sellsbrothers.com/12503