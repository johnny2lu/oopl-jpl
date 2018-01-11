# -----------
# Wed, 10 Jan
# -----------

"""
assertions are good for preconditions and postconditions
they're not good for user errors, instead exceptions
they're not good for testing, instead unittest

tests are only as good as the coverage that they achieve

exceptions
try, except, else, finally
what was the concern with except clause that are trying to handle types in a class hierarchy
"""

x = 2         # int, a value
x = [2, 3, 4] # list, an address

# simple types
int
bool
float

# composite types
list  # implemented with a front-loaded array
tuple # like list, but immutable
set   # like list, but no duplicates and order doesn't matter
dict  # list set,  but it has keys AND values
deque # doubly-linked list, very different complexities to an array

print([2, 3, 4] is [2, 3, 4]) # false
print([2, 3, 4] == [2, 3, 4]) # true
print([2, 3, 4] == [2, 4, 3]) # false

print({2, 3, 4} is {2, 3, 4}) # false
print({2, 3, 4} == {2, 3, 4}) # true
print({2, 3, 4} == {2, 4, 3}) # true

# operators
# + vs +=
# expressions vs statement

x = ()

# list's += is okay with any iterable on the right-hand-side

# tuple's += is NOT okay with any iterable on the right-hand-side
# it must be another tuple

x += y

# is that the same as (yes, for immutables and no for mutable)

x = x + y

x + ?

# list's + is NOT okay with any iterable on the right-hand-side
# it must be another list

# tuple's + is NOT okay with any iterable on the right-hand-side
# it must be another tuple

for v in range(2, 5) :
    print(v)           # 2 3 4

# this is what's really happening

p = iter(range(2, 5))
try :
    while True :
        v = next(p)
        print(v)
except StopIteration :
    pass

p = iter(range(2, 5))
print(type(p))        # range iterator
print(next(p))        # 2
print(next(p))        # 3
print(next(p))        # 4
print(next(p))        # StopIteration exception

def add (x, y) :
    return x + y

def mul (x, y) :
    return x * y

"""
reduce takes three arguments
first  argument: is a binary function
second argument: an iterable
third  argument: a value
"""

def factorial_range_reduce (n: int) -> int :
    assert n >= 0
    return reduce(lambda x, y : x * y, range(1, n + 1), 1)

x     = (2, 3, 4)
x[1] += 1          # not ok

x    = (2, [3], 4)
x[1] = [1]         # not ok

x[1] += [1]        # ok!!!

print(x)           # (2, [3, 1], 4)

x = [2, 3, 4]
y = x

x += [5]

print(x is y) # true

x = (2, 3, 4)
y = (2, 3, 4)
print(x is y) # false

class A :
    def f (self) :
        ...

    def __iter__ (self) :
        ...

    def __getitem__ (self, i) :
        ...

x = A()              # my type
x.f()
p = iter(x)          # this means A is iterable
p = x.__iter__()     # p = iter(x) really means
v = x[5]
v = x.__getitem__(5) # v = x[5] really means

a = [2, 3, 4]
b = a[:]      # copy, NOT the same as b = a
print(a is b) # false

a = (2, 3, 4)
b = a[:]      # copy, the same b = a
print(a is b) # true

x = [2, 3, 4]
print(type(x))                # list
print(hasattr(x, "__next__")) # false

p = iter(x)
print(type(p))                # list iterator
print(hasattr(p, "__next__")) # true

for v in [(2, 3), (4, 5), (6, 7)] :
    print(v)                        # (2, 3) (4, 5) (6, 7)

for u, v in [(2, 3), (4, 5), (6, 7)] :
    print(u)                           # 2 4 6
    print(v)                           # 3 5 7

for u, v in z : # z has to be an iterable of iterables of length 2
    ...

for u, _, w, _ in z :
    ...

print([2, 3, 4] == [2, 3, 4]) # true
print([2, 3, 4] == [2, 4, 3]) # false

print({2, 3, 4} == {2, 3, 4}) # true
print({2, 3, 4} == {2, 4, 3}) # true
