title = "Bitbucket to Github with Branches and Tags"
date = 2022-01-06T17:47:00+02:00
tags = [
    "Github",
    "Bitbucket",
    "branch",
    "tag",
    "move",
    "migration"
]
published = true
+++++

1) Create  a new folder where we will clone fresh copies of the remote repo.

2) Clone the repo using the following
```
git clone --mirror git@bitbucket.com:org/name.git
```

3) Navigate into the locally cloned repo.
```
cd name.git/
```

4) Set the new remote
```
git remote set-url --push origin git@github.com:org/name.git
```

5) Push the contents of the repo to the new remote.
```
git push --mirror
```

Enjoy!