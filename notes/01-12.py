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
























