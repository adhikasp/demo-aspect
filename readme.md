# demo-aspect

This is a example project that will run coala with the brand new aspect
setting.

## Requirement

- Install coala from branch adhikasp/collect-bears
- Install coala-bears from branch demo-aspect

## In action

This repo contain `demo-aspect.py`, a snippet code that contain
**unused import** and **unused local variable**. The `.coafile` contain
configuration to search **redundant** code in `.py` files.

The desired result is the `cos` import got removed by coala using
`PyUnusedCodeBear` even though we don't explicitly tell coala to use it.

### Result

```
$ coala

...

**** PyUnusedCodeBear [Section: python] ****

!    ! [Severity: NORMAL]
!    ! This file contains unused source code.
[----] /home/dhika/Workspace/demo-aspect/demo-aspect.py
[++++] /home/dhika/Workspace/demo-aspect/demo-aspect.py
[    ] Line affected 1
[    ] 
[----] from math import sin, cos
[++++] from math import sin
[    ] Do (N)othing
[    ] (O)pen file
[    ] (A)pply patch
[    ] Add (I)gnore comment
[    ] (C)hain actions
[    ] Enter number (Ctrl-D to exit): n
```