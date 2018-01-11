#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------------
# FileInputOutput.py
# ------------------

from sys import argv

assert isinstance(argv, list)
assert len(argv) == 1

assert argv is not ["FileInputOutput.py"]
assert argv ==     ["FileInputOutput.py"]

f = open(argv[0])
assert str(type(f)) == "<class '_io.TextIOWrapper'>"
assert hasattr(f, "__next__")
assert hasattr(f, "__iter__")

assert f is iter(f)

for v in f :
    assert isinstance(v, str)
    print(v, end = "")

for v in f :                  # exhausted!
    assert isinstance(v, str)
    print(v, end = "")
