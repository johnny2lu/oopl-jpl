#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = too-few-public-methods

# --------
# Map1T.py
# --------

# https://docs.python.org/3/library/functions.html#map

from timeit   import timeit
from unittest import main, TestCase
from typing   import Callable, Iterable, Iterator, TypeVar

T = TypeVar("T")

# 605 milliseconds
class map_iterator (Iterator[T]) :
    def __init__ (self, uf: Callable[[T], T], a: Iterable[T]) -> None :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) -> Iterator[T] :
        return self

    def __next__ (self) -> T :
        return self.uf(next(self.p))

# 380 milliseconds
def map_for (uf: Callable[[T], T], a: Iterable[T]) -> Iterator[T] :
    for v in a :
        yield uf(v)

# 376 milliseconds
def map_generator (uf: Callable[[T], T], a: Iterable[T]) -> Iterator[T] :
    return (uf(v) for v in a)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_iterator,
            map_for,
            map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(lambda v : v ** 2, [2, 3, 4])
                self.assertEqual(list(m), [4, 9, 16])
                self.assertEqual(list(m), [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(lambda v : v ** 3, {2, 3, 4})
                self.assertEqual(list(m), [8, 27, 64])
                self.assertEqual(list(m), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(None, ())
                self.assertEqual(list(m), [])

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "map" :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda v : v ** 2, 10000 * [5]))",
                        "",
                        number = 100)
                else :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda v : v ** 2, 10000 * [5]))",
                        "from __main__ import " + f.__name__,
                        number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" : # pragma: no cover
    main()

""" #pragma: no cover
% MapT.py
..
map_iterator
605.10 milliseconds

map_for
380.03 milliseconds

map_generator
375.83 milliseconds

map
295.65 milliseconds
.
----------------------------------------------------------------------
Ran 3 tests in 2.061s

OK
"""
