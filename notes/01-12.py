# -----------
# Fri, 12 Jan
# -----------

"""
"""

x = [2, 3, 4]
y = [v + 1 for v in x]
print(y)               # [3, 4, 5]

x = [2, 3, 4]
y = (v + 1 for v in x)
print(y)               # <address of the generator>
v = next(y)
print(v)               # 3

x = [2, 3, 4]
y = (v + 1 for v in x)
print(list(y))         # [3, 4, 5]
print(list(y))         # []

x = [2, 3, 4]
y = (v + 1 for v in x)
x =+ [5]
print(list(y))         # [3, 4, 5, 6]
print(list(y))         #

x = (2, 3, 4)
y = (v + 1 for v in x)
x =+ [5]
print(list(y))         # [3, 4, 5]
print(list(y))         # []

def f () :
    print("abc")
    yield 2
    print("def")
    yield 3

x = f()     # <nothing prints>
print(x)    # <address of the generator>
v = next(x) # abc
print(v)    # 2
w = next(x) # def
print(w)    # 3
t = next(x) # raises StopIteration

v = f(x)
v = f.__call__(x)

# function

def f (z) :
    ...

# class

class f :
    def __init__ (self, z) :
        ...

# instance of a class that has __call__

class foo :
    def __call__ (self, z) :
        ...

f = foo()

x = f4()
print(list(x)) # [2, 3, 4]
print(list(x)) # []

print(list(f4())) # [2, 3, 4]
print(list(f4())) # [2, 3, 4]

"""
three tokens
    =
    *
    **

two contexts
    a function call
    a function definition
"""

print(2, end=" ")

def f (a, b, *c) :
    if c == () :
    if not c :

def f (a, b, c = None) :
    if c == None :

f(2, 3)
f(2, 3, 4)
f(2, 3, None)

# instance variable

class A :
    def __init__ (self, v) :
        self.v = v           # instance variable

x = A(2)
print(x.v) # 2

y = A(3)
print(y.v) # 3

# instance variable

class A :
    def f (self, v) :
        self.v = v    # instance variable

x = A()
print(x.v) # not ok
x.f(2)
print(x.v) # 2

y = A()
print(y.v) # not ok

# class variable

class A :
    v = 2

print(A.v) # 2

class A :
    cv = 5

    def __init__ (self, v) :
        self.v = v

    @staticmethod
    def sm (w) :
        ...

A.sm(2)
