

Sometimes your terminal is slow. How do you debug it? Lets find out. 


Lets enable printing of all the commands run when you enter a new command:

```
set -x
```

and stop the debug process via:
```
set +x
```

Sources:
 - https://unix.stackexchange.com/a/565927