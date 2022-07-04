# playwright-python-memleak-test
A little test loop to see about playwright pythons memory leak (or not)

Trying to resolve https://github.com/microsoft/playwright/issues/6319

I know that I can see it in my application, somehow it's a real bug, but I can't get to the bottom of it

```

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                                                                                     
3235437 root      20   0  709296 268132   6528 S   0.0   1.6   2:59.25 python                                                                                                      
4068971 root      20   0  664868 256592   6764 S   0.0   1.6   2:30.59 python   
```
