#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring
# pylint: disable = too-many-locals
# pylint: disable = too-many-statements
# pylint: disable = unused-import

# ------------
# Operators.py
# ------------

# https://docs.python.org/3/library/operator.html
# https://graphics.stanford.edu/~seander/bithacks.html

from typing import Tuple

from operator import add

def test () :
    i = 2
    j = -i         # negation
    assert i ==  2
    assert j == -2

    i = 2
    j = 3
    i = j         # assignment
    assert i == 3
    assert j == 3

    i = 2
    j = 3
    k = i + j     # addition
    assert i == 2
    assert j == 3
    assert k == 5

    i = 2
    j = 3
    k = add(i, j)
    assert i == 2
    assert j == 3
    assert k == 5

    i = 2
    j = 3
    i += j        # in-place addition
    assert i == 5
    assert j == 3

    i = 4
    j = 2
    f = i / j                   # true division
    assert i == 4
    assert j == 2
    assert isinstance(f, float)
    assert str(f) == "2.0"

    g =  4                      # type: float
    j =  2
    g /= j
    assert isinstance(g, float)
    assert str(g) == "2.0"
    assert j      == 2

    i = 5
    j = 2
    k = i // j                # floor division
    assert i == 5
    assert j == 2
    assert isinstance(k, int)
    assert k == 2

    i = 5
    j = 2
    i //= j
    assert isinstance(i, int)
    assert i == 2
    assert j == 2

    f = 5.0
    j = 2
    g = f // j                  # floor division
    assert f == 5.0
    assert j == 2
    assert isinstance(g, float)
    assert str(g) == "2.0"

    f = 5.0
    j = 2
    f //= j
    assert isinstance(f, float)
    assert str(f) == "2.0"
    assert j      == 2

    i = 12
    j = 10
    k = i % j      # mod
    assert i == 12
    assert j == 10
    assert k ==  2

    i = 12
    j = 10
    i %= j
    assert i ==  2
    assert j == 10

    i = 2
    j = 3
    k = i ** j    # exponentiation
    assert i == 2
    assert j == 3
    assert k == 8

    i = 2
    j = 3
    i **= j
    assert i == 8
    assert j == 3

    i = 2
    j = 3
    k = i << j     # bit shift left
    assert i ==  2
    assert j ==  3
    assert k == 16

    i = 2
    j = 3
    i <<= j
    assert i == 16
    assert j ==  3

    i = 10          # 0000 0000 0000 1010
    j = ~i          # 1111 1111 1111 0101: bit complement
    k = ~i + 1      # 1111 1111 1111 0110
    assert i ==  10
    assert j == -11
    assert k == -10

    i = 10         # 1010
    j = 12         # 1100
    k = i & j      # 1000: bit and
    assert i == 10
    assert j == 12
    assert k ==  8

    i = 10
    j = 12
    i &= j
    assert i ==  8
    assert j == 12

    i = 10         # 1010
    j = 12         # 1100
    k = i | j      # 1110: bit or
    assert i == 10
    assert j == 12
    assert k == 14

    i = 10
    j = 12
    i |= j
    assert i == 14
    assert j == 12

    i = 10         # 1010
    j = 12         # 1100
    k = i ^ j      # 0110: bit exclusive or
    assert i == 10
    assert j == 12
    assert k ==  6

    i = 10
    j = 12
    i ^= j
    assert i ==  6
    assert j == 12

    i = 10         # 1010
    j = 12         # 1100
    i ^= j
    assert i ==  6 # 0110
    assert j == 12 # 1100
    j ^= i
    assert i ==  6 # 0110
    assert j == 10 # 1010
    i ^= j
    assert i == 12 # 1100
    assert j == 10 # 1010

    i = 10
    j = 12
    i += j
    assert i == 22
    assert j == 12
    j = i - j
    assert i == 22
    assert j == 10
    i -= j
    assert i == 12
    assert j == 10

    i = 10
    j = 12
    i, j = j, i
    assert i == 12
    assert j == 10

    i = 3
    j = 5
    k = 7
    l = 8
    assert (i < j) and (j < k) and (k < l)
    assert i < j < k < l

    p = True
    q = True
    r = False
    assert p and q
    assert not (p and r)
    assert p or q

    s = "abc"
    assert s[1] == "b"
    #s[1] = "d"        # TypeError: 'str' object does not support item assignment

    a = [2, 3, 4]
    assert a[1] == 3 # list index
    a[1] += 1
    assert a[1] == 4

    u = (2, 3, 4)    # type: Tuple
    assert u[1] == 3 # tuple index
    #u[1] += 1       # TypeError: 'tuple' object does not support item assignment

    s = "a"
    t = "bc"
    m = s + t             # string concatenation
    assert m is not "abc"
    assert m ==     "abc"

    a = [2]
    b = [3, 4]
    c = a + b                 # list concatenation
    assert c is not [2, 3, 4]
    assert c ==     [2, 3, 4]
    assert c !=     (2, 3, 4)

    u = (2,)
    v = (3, 4)                # type: Tuple
    w = (u + v)               # tuple concatenation
    assert w is not (2, 3, 4)
    assert w ==     (2, 3, 4)
    assert w !=     [2, 3, 4]

    s = "abc"
    t = 2 * s                # string replication
    assert t is not "abcabc"
    assert t ==     "abcabc"

    a = [2, 3, 4]
    b = 2 * a                          # list replication
    assert b is not [2, 3, 4, 2, 3, 4]
    assert b ==     [2, 3, 4, 2, 3, 4]

    u = (2, 3, 4)
    v = 2 * u                          # tuple replication
    assert u is not (2, 3, 4, 2, 3, 4)
    assert v ==     (2, 3, 4, 2, 3, 4)


if __name__ == "__main__" : # pragma: no cover
    print("Operators.py")
    test()
    print("Done.")
