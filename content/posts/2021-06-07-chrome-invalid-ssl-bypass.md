title = "How to bypass an Invalid Cert in Chrome - Your connection is not private"
date = 2021-06-07T00:00:00+02:00
tags = [
    "chrome",
    "tls",
    "ssl",
    "cert"
]
published = true
+++++

Story:
Recently I have noticed that the `Proceed to www...com (unsafe)` link in Chrome has stopped appearing on webpages with invalid certs. I use self sign certs for local development quite often so this is kind of a big issue.

**Problem:**
The `Proceed to www...com (unsafe)` link no long shows up on pages with invalid certs. Therefore, I can not access the local sites I am developing.

**Solution:**
Click somewhere on the denial page and type in `thisisunsafe`. That will prevent this error for that URL for the foreseeable future.
