#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------
# Map1.py
# -------

# https://docs.python.org/3/library/functions.html#map

def test () -> None :
    a = (2, 3, 4)

    m = map(lambda v : v ** 2, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

    p = 2
    m = map(lambda v : v ** p, a)
    assert list(m) == [4, 9, 16]
    assert list(m) == []

if __name__ == "__main__" : # pragma: no cover
    print("Map1.py")
    test()
    print("Done.")
