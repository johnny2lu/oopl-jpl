#!/usr/bin/env python3

# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = bad-whitespace

# --------
# Hello.py
# --------

# https://www.python.org
# https://docs.python.org/3.6/
# https://docs.python.org/3.6/library/
# https://www.python.org/dev/peps/pep-0008/
# http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html

if __name__ == "__main__" :      # pragma: no cover
    print("Nothing to be done.")

""" #pragma: no cover
Developed in 1989 by Guido van Rossum of the Netherlands, now at Dropbox.
Python is procedural, object-oriented, dynamically typed, and garbage collected.



% which python3
/usr/local/bin/python3



% python3 --version
Python 3.6.3



% python3 -- help
...



% python3 Hello.py
Nothing to be done.



% chmod ugo+x Hello.py
% ./Hello.py
Nothing to be done.



% python3
Python 3.6.3 (default, Oct  4 2017, 06:09:38)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.



>>> import Hello
Nothing to be done.



>>> quit()



% python3
Python 3.6.3 (default, Oct  4 2017, 06:09:38)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".



help> range
...



help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.

>>> quit()



% python3
Python 3.6.3 (default, Oct  4 2017, 06:09:38)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!



>>> from __future__ import braces
  File "<stdin>", line 1
SyntaxError: not a chance



>>> import antigravity
...



>>> quit()
"""
