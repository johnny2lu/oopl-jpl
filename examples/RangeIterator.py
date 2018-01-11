#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------------
# RangeIterator.py
# ----------------

def f (b, e) :
    return iter(range(b, e))

def test () -> None :
    p = f(2, 2)
    assert p is iter(p)
    try :
        next(p)
    except StopIteration :
        pass

    p = f(2, 3)
    assert p is iter(p)
    assert next(p) == 2
    try :
        next(p)
    except StopIteration :
        pass

    p = f(2, 4)
    assert p is iter(p)
    assert next(p) == 2
    assert next(p) == 3
    try :
        next(p)
    except StopIteration :
        pass

    p = f(2, 5)
    assert list(p) == [2, 3, 4]
    assert list(p) == []

if __name__ == "__main__" : # pragma: no cover
    print("RangeIterator.py")
    test()
    print("Done.")
