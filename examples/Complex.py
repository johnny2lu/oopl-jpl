#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ----------
# Complex.py
# ----------

# https://docs.python.org/3/library/functions.html#complex
# https://docs.python.org/3/reference/datamodel.html

def test () :
    x = complex()
    assert x.real == 0
    assert x.imag == 0

    x = complex(2)
    assert x.real == 2
    assert x.imag == 0

    x = complex(2, 3)
    assert x.real == 2
    assert x.imag == 3

    x = complex(2, 3)
    assert x != (2, 3)         # x.__eq__((2, 3))
    assert x == complex(2, 3)  # x.__eq__(complex(2, 3)

    x = complex(2, 3)
    s = str(x)                 # x.__str__()
    assert s == "(2+3j)"
    x = complex(-2, -3)
    s = str(x)                 # x.__str__()
    assert s == "(-2-3j)"

    x = complex(2, 3)
    # y = x + (4, 5)           # TypeError: unsupported operand type(s) for +: 'complex' and 'tuple'
    y = x + complex(4, 5)      # y = x.__add__(complex(4, 5))
    assert x == complex(2, 3)
    assert y == complex(6, 8)

    x  = complex(2, 3)
    y  = x
    # x += (4, 5)              # TypeError: unsupported operand type(s) for +=: 'complex' and 'tuple'
    x += complex(4, 5)         # x = x.__add__(complex(4, 5))
    assert x == complex(6, 8)
    assert y == complex(2, 3)

    x = complex(4, 5)
    # y = x - (2, 3)           # TypeError: unsupported operand type(s) for -: 'complex' and 'tuple'
    y = x - complex(2, 3)      # y = x.__sub__(complex(2, 3))
    assert x == complex(4, 5)
    assert y == complex(2, 2)

    x  = complex(4, 5)
    y  = x
    # x -= (2, 3)              # TypeError: unsupported operand type(s) for -=: 'complex' and 'tuple'
    x -= complex(2, 3)         # x = x.__isub__(complex(2, 3))
    assert x == complex(2, 2)
    assert y == complex(4, 5)

    x = complex(2, 3)
    y = x.conjugate()
    assert x == complex(2,  3)
    assert y == complex(2, -3)

if __name__ == "__main__" : # pragma: no cover
    print("Complex.py")
    test()
    print("Done.")
