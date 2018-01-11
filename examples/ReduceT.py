#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# Reduce1T.py
# -----------

# https://docs.python.org/3.6/library/functools.html

from functools import reduce
from operator  import add, concat, mul
from typing    import Callable, Iterable, Sequence, TypeVar
from unittest  import main, TestCase

T = TypeVar("T")

def reduce_for_range (bf: Callable[[T, T], T], a: Sequence[T], v: T) -> T :
    for i in range(len(a)) :
        w = a[i]
        v = bf(v, w)
    return v

def reduce_for (bf: Callable[[T, T], T], a: Iterable[T], v: T) -> T :
    for w in a :
        v = bf(v, w)
    return v

def reduce_while (bf: Callable[[T, T], T], a: Iterable[T], v: T) -> T :
    p = iter(a)
    try :
        while True :
            w = next(p)
            v = bf(v, w)
    except StopIteration :
        pass
    return v

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            reduce_for_range,
            reduce_for,
            reduce_while,
            reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(add, [2, 3, 4], 0), 9)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                if f != reduce_for_range :
                    self.assertEqual(f(mul, {2, 3, 4}, 1), 24)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(concat, ("a", "b", "c"), ""), "abc")

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(f(None, {}, 2),  2)

if __name__ == "__main__" : # pragma: no cover
    main()
