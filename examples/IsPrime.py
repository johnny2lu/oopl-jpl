#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# IsPrime.py
# ----------

from math import sqrt

def is_prime (n: int) -> bool :
    assert n > 0
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0 :
            return False
    return True

def test () -> None :
    assert not is_prime(1)
    assert not is_prime(2)
    assert     is_prime(3)
    assert not is_prime(4)
    assert     is_prime(5)
    assert     is_prime(7)
    assert     is_prime(9)
    assert not is_prime(27)
    assert     is_prime(29)

if __name__ == "__main__" : # pragma: no cover
    print("IsPrime.py")
    test()
    print("Done.")
