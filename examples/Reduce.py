#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Reduce.py
# ---------

# https://docs.python.org/3.6/library/functools.html

from functools import reduce
from operator  import add, mul, sub

def test () -> None :
    assert reduce(add,  [2, 3, 4], 0) == 9
    assert reduce(mul,  (2, 3, 4), 1) == 24
    assert reduce(sub,  {2, 3, 4}, 2) == -7
    assert reduce(None, [],        3) == 3

if __name__ == "__main__" : # pragma: no cover
    print("Reduce.py")
    test()
    print("Done.")
