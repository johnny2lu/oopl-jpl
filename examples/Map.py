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
    m = map(lambda v : v ** 2, [2, 3, 4])
    assert hasattr(m, "__next__")
    assert hasattr(m, "__iter__")
    assert iter(m) is m
    assert list(m) == [4, 9, 16]
    assert list(m) == []

    m = map(lambda v : v ** 3, {2, 3, 4})
    assert list(m) == [8, 27, 64]
    assert list(m) == []

    m = map(None, ())
    assert list(m) == []

if __name__ == "__main__" : # pragma: no cover
    print("Map.py")
    test()
    print("Done.")
