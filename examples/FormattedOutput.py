#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------------
# FormattedOutput.py
# ------------------

# https://docs.python.org/3.5/library/stdtypes.html#printf-style-string-formatting

print("FormattedOutput.py")

pi = 3.14159

s = "%7.2f" % pi          # must be an object or a tuple
assert isinstance(s, str)
assert s is not "   3.14"
assert s ==     "   3.14"

s = "%7.2f, %7.2f" % (pi, pi)      # must be an object or a tuple
assert isinstance(s, str)
assert s is not "   3.14,    3.14"
assert s ==     "   3.14,    3.14"

s = "%7.3f" % pi
assert isinstance(s, str)
assert s is not "  3.142"
assert s ==     "  3.142"

s = "%-7.3f" % pi
assert isinstance(s, str)
assert s is not "3.142  "
assert s ==     "3.142  "

s = "%10.6f" % pi
assert isinstance(s, str)
assert s is not "  3.141590"
assert s ==     "  3.141590"

# s = "%7.2f, %7.2f" % [pi, pi] # TypeError: a float is required

# s = "%7.2f" % (pi, pi) # TypeError: not all arguments converted during string formatting

# s = "%7.2f, %7.3f" % pi # TypeError: not enough arguments for format string

# s = "%7.2f, %7.3f" % (pi, "abc") # TypeError: a float is required

print("Done.")
