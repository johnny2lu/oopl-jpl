#!/usr/bin/env python3

# pylint: disable = bad-continuation
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# https://docs.python.org/3/library/functools.html

# -----------
# Reduce2T.py
# -----------

from functools import reduce
from operator  import add, mul, sub
from typing    import Callable, Iterable, TypeVar
from unittest  import main, TestCase

T = TypeVar("T")

def my_reduce (bf: Callable[[T, T], T], a: Iterable[T], *vs: T) -> T:
    p = iter(a)
    if not vs :
        if not a :
            raise TypeError("reduce() of empty sequence with no initial value")
        v = next(p)
    else :
        v = vs[0]
    for w in p :
        v = bf(v, w)
    return v

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
               reduce,
            my_reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2, 3, 4], 0), 9)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(mul, (2, 3, 4), 1), 24)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(sub, {2, 3, 4}, 2), -7)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, [], 3), 3)

    def test_5 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2, 3, 4]), 9)

    def test_6 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(mul, (2, 3, 4)), 24)

    def test_7 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(sub, {2, 3, 4}), -5)

    def test_8 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, [3]), 3)

    def test_9 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertRaises(TypeError, f, None, [])

if __name__ == "__main__" : # pragma: no cover
    main()
