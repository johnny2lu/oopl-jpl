#!/usr/bin/env python3

# pylint: disable = bad-continuation
# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = line-too-long
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -----------
# ComplexT.py
# -----------

# https://docs.python.org/3/library/functions.html#complex
# https://docs.python.org/3/reference/datamodel.html

from unittest import main, TestCase

class my_complex :
    def __init__ (self, real: int = 0, imag: int = 0) -> None :
        self.real = real
        self.imag = imag

    def __add__ (self, rhs) -> "my_complex" :
        if not isinstance(rhs, my_complex) :
            raise TypeError
        return my_complex(self.real + rhs.real, self.imag + rhs.imag)

    def __eq__ (self, rhs) -> bool :
        if not isinstance(rhs, my_complex) :
            return False
        return (self.real == rhs.real) and (self.imag == rhs.imag)

    def __str__ (self) -> str :
        return ("(%s%sj)" if self.imag < 0 else "(%s+%sj)") % (self.real, self.imag)

    def __sub__ (self, rhs) -> "my_complex" :
        if not isinstance(rhs, my_complex) :
            raise TypeError
        return my_complex(self.real - rhs.real, self.imag - rhs.imag)

    def __isub__ (self, rhs) -> "my_complex" :
        if not isinstance(rhs, my_complex) :
            raise TypeError
        return my_complex(self.real - rhs.real, self.imag - rhs.imag)

    def conjugate (self) -> "my_complex" :
        return my_complex(self.real, -self.imag)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
               complex,
            my_complex]

    def test_01 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c()
                self.assertEqual(x.real, 0)
                self.assertEqual(x.imag, 0)

    def test_02 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(2)
                self.assertEqual(x.real, 2)
                self.assertEqual(x.imag, 0)

    def test_03 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(2, 3)
                self.assertEqual(x.real, 2)
                self.assertEqual(x.imag, 3)

    def test_04 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(2, 3)
                self.assertNotEqual(x, (2, 3)) # x.__eq__((2, 3))
                self.assertEqual(x, c(2, 3))   # x.__eq__(c(2, 3))

    def test_05 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(2, 3)
                s = str(x)                     # x.__str__()
                self.assertEqual(s, "(2+3j)")
                x = c(-2, -3)
                s = str(x)                     # x.__str__()
                self.assertEqual(s, "(-2-3j)")

    def test_06 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(2, 3)
                # y = x + (4, 5)             # TypeError: unsupported operand type(s) for +: 'complex' and 'tuple'
                y = x + c(4, 5)              # y = x.__add__(c(4, 5))
                self.assertEqual(x, c(2, 3))
                self.assertEqual(y, c(6, 8))

    def test_07 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x  = c(2, 3)
                y  = x
                # x += (4, 5)                # TypeError: unsupported operand type(s) for +=: 'complex' and 'tuple'
                x += c(4, 5)                 # x = x.__add__(c(4, 5))
                self.assertEqual(x, c(6, 8))
                self.assertEqual(y, c(2, 3))

    def test_08 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(4, 5)
                # y = x - (2, 3)             # TypeError: unsupported operand type(s) for -: 'complex' and 'tuple'
                y = x - c(2, 3)              # y = x.__sub__(c(2, 3))
                self.assertEqual(x, c(4, 5))
                self.assertEqual(y, c(2, 2))

    def test_09 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x  = c(4, 5)
                y  = x
                # x -= (2, 3)                # TypeError: unsupported operand type(s) for -=: 'complex' and 'tuple'
                x -= c(2, 3)                 # x = x.__isub__(c(2, 3))
                self.assertEqual(x, c(2, 2))
                self.assertEqual(y, c(4, 5))

    def test_10 (self) :
        for c in self.a :
            with self.subTest(msg=c.__name__) :
                x = c(2, 3)
                y = x.conjugate()
                self.assertEqual(x, c(2,  3))
                self.assertEqual(y, c(2, -3))

if __name__ == "__main__" : # pragma: no cover
    main()
