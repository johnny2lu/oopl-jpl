#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = function-redefined
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = redefined-outer-name
# pylint: disable = singleton-comparison
# pylint: disable = too-few-public-methods
# pylint: disable = too-many-locals
# pylint: disable = unused-import

# --------
# Types.py
# --------

# https://docs.python.org/3.6/library/types.html

from collections import deque
from typing      import Dict, FrozenSet, List, Set, Tuple
from types       import FunctionType

def test () :
    b = bool()
    assert b == False
    b = bool(True)
    b = True
    assert b
    assert not False
    assert isinstance(b,    bool)
    assert isinstance(bool, type)
    assert issubclass(bool, bool)
    assert issubclass(bool, object)

    i = int()
    assert i == 0
    i = int(2)
    i = 2
    assert i
    assert not 0
    assert isinstance(i,   int)
    assert isinstance(int, type)
    assert issubclass(int, int)
    assert issubclass(int, object)

    assert     issubclass(bool, int)
    assert not issubclass(int,  bool)

    f = float()
    assert f == 0.0
    f = float(2.3)
    f = 2.3
    assert f
    assert not 0.0
    assert isinstance(f,     float)
    assert isinstance(float, type)
    assert issubclass(float, float)
    assert issubclass(float, object)

    c = complex()
    assert c == 0 + 0j
    c = complex(2, 3)
    c = 2 + 3j
    assert c
    assert not 0 + 0j
    assert isinstance(c,       complex)
    assert isinstance(complex, type)
    assert issubclass(complex, complex)
    assert issubclass(complex, object)

    s = str()
    assert s == ""
    s = str("abc")
    s = "abc"
    assert s
    assert not ""
    assert isinstance(s,   str)
    assert isinstance(str, type)
    assert issubclass(str, str)
    assert issubclass(str, object)

    a = list()                      # type: List
    assert a == []
    a = list([2, 3, 4])
    a = [2, 3, 4]
    assert a
    assert not []
    assert isinstance(a,    list)
    assert isinstance(list, type)
    assert issubclass(list, list)
    assert issubclass(list, object)

    u = tuple()                      # type: Tuple
    assert u == ()
    u = tuple((2, "abc", 3.45))
    u = (2, "abc", 3.45)
    assert u
    assert not ()
    assert isinstance(u,     tuple)
    assert isinstance(tuple, type)
    assert issubclass(tuple, tuple)
    assert issubclass(tuple, object)

    x = set()                       # type: Set
    x = set({2, 3, 4})
    x = {2, 3, 4}
    assert x
    assert not set()
    assert isinstance(x,   set)
    assert isinstance(set, type)
    assert issubclass(set, set)
    assert issubclass(set, object)

    y = frozenset()                         # type: FrozenSet
    y = frozenset({2, 3, 4})
    assert y
    assert not frozenset()
    assert isinstance(y,         frozenset)
    assert isinstance(frozenset, type)
    assert issubclass(frozenset, frozenset)
    assert issubclass(frozenset, object)

    d = dict()                                       # type: Dict
    assert d == {}
    d = dict({2: "abc", 3: "def", 4: "ghi"})
    d = {2: "abc", 3: "def", 4: "ghi"}
    assert d
    assert not {}
    assert isinstance(d,    dict)
    assert isinstance(dict, type)
    assert issubclass(dict, dict)
    assert issubclass(dict, object)

    q = deque()                      # type: deque
    q = deque((2, 3, 4))             # FIFO or LIFO queue
    assert q
    assert not deque()
    assert isinstance(q,    deque)
    assert isinstance(deque, type)
    assert issubclass(deque, deque)
    assert issubclass(deque, object)

    def g (v) :
        return v + 1
    assert g
    assert isinstance(g,            FunctionType)
    assert isinstance(FunctionType, type)
    assert issubclass(FunctionType, FunctionType)
    assert issubclass(FunctionType, object)

    h = lambda v : v + 1
    assert h
    assert isinstance(h,            FunctionType)
    assert isinstance(FunctionType, type)
    assert issubclass(FunctionType, FunctionType)
    assert issubclass(FunctionType, object)

    class A :
        def __init__ (self, i, f) :
            pass

    assert A
    assert isinstance(A, type)
    assert isinstance(A, object)
    assert issubclass(A, A)
    assert issubclass(A, object)

    z = A(2, 3.45)

    assert z
    assert isinstance(z, A)
    assert isinstance(z, object)

    class B :
        def __bool__ (self) :
            return False

    t = B()
    assert not t

    assert isinstance(type,   type)
    assert isinstance(type,   object)
    assert isinstance(object, object)

if __name__ == "__main__" : # pragma: no cover
    print("Types.py")
    test()
    print("Done.")
