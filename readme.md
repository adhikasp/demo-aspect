# demo-aspect

This is a example project that will run coala with the brand new aspect
setting.

## Requirement

- Install [coala](https://github.com/coala/coala)
- Install [coala-bears](https://github.com/coala/coala-bears)

## In action

This repo contain `demo-aspect.py`, a snippet code that contain
**unused import** and **unused local variable**. The `.coafile` contain
configuration to search **redundant** code in `.py` files.

The desired result is the `cos` import got removed by coala using
`PyUnusedCodeBear`, and ignoring `UnusedButNonStandardPackage` and `x` unused
variable.

### Result

```
$ coala

...

**** PyUnusedCodeBear [Section: python] ****
demo-aspect.py
[   2] from·math·import·sin,·cos
**** PyUnusedCodeBear [Section: aspect | Severity: NORMAL] ****
!    ! This file contains unused source code.
[----] /home/dhika/Workspace/demo-aspect/demo-aspect.py
[++++] /home/dhika/Workspace/demo-aspect/demo-aspect.py
[   2] from math import sin, cos
[   2] from math import sin
[    ] *0. Do (N)othing
[    ]  1. (O)pen file
[    ]  2. (A)pply patch
[    ]  3. Print (M)ore info
[    ]  4. Add (I)gnore comment
[    ]  5. Show Applied (P)atches
[    ]  6. (G)enerate patches
[    ] Enter number (Ctrl-D to exit):
```
