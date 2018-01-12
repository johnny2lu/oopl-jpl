#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# https://docs.python.org/3/library/functools.html

# ----------
# Reduce2.py
# ----------

from functools import reduce
from operator  import add, mul

def test () -> None :
    assert reduce(add, [2, 3, 4],  0) == 9
    assert reduce(mul, [2, 3, 4],  1) == 24

    assert reduce(add, {2, 3, 4})     == 9
    assert reduce(mul, {2, 3, 4})     == 24

    assert reduce(None, [],        2) == 2
    assert reduce(None, [2])          == 2

    try :
        reduce(None, [])
    except TypeError :
        pass

if __name__ == "__main__" : # pragma: no cover
    print("Reduce2.py")
    test()
    print("Done.")
