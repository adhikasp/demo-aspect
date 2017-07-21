# Unused import!! Remove cos
from math import sin, cos
# not removing this because we can set ``remove_only_standard_package`` taste!
import UnusedButNonStandardPackage

def foo():
    # Unused and can be removed.
    # BUT, not removed because we exlude UnusedLocalVariable
    x = 1
    return sin(5)
