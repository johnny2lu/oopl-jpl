# -----------
# Thu, 11 Jan
# -----------

"""
how Python inherently treat mutable objects differently than immutable

x = []
loop
    x += ? # amortized const

x = ()
loop
    x += ? # linear

Python rewards you for programming in a Pythonic way

building the obvious while for factorial() was twice as slow
as using the Python for in idiom

a higher-order function, which is a function that takes a function as an argument
or returns a function as a result

reduce is a nice abstraction, whose special cases involve: sum, product, and factorial

caches literals and small-valued integers [-5, 256]

a = [2, 3, 4]
b = [5, a, 6]

when writing an algorithm you want to be as undemanding possible

being indexable is a stronger and harder quality to have than just being
iterable

indexable implies iterable, not the other way around

list, tuple, str: indexable and iterable
set: iterable, not indexable

when writing a container you want to provide the strongest quality
"""

x = [2, 3, 4]
print(type(x))                # list
print(hasattr(x, "__next__")) # false
print(hasattr(x, "__iter__")) # true

p = iter(x)
print(type(p))                # list iterator
print(hasattr(x, "__next__")) # true
print(hasattr(x, "__iter__")) # true

print(x is p)  # false

q = iter(p)
print(type(q))                # list iterator
print(p is q)  # true

"""
iterables: list, tuple, str, set, deque, dict, range
iterators: iter(<on any iterable>), count, zip
"""

x = list(<iterable>)
x = set(<iterable>)
x = deque(<iterable>)

x = [2, 3, 4]
y = x
print(x is y) # true

y = x[:]
print(x is y) # false

y = copy(x)
print(x is y) # false

y = list(x)
print(x is y) # false

x = f(...)

# print the square of each element
x = [2, 3, 4]
for v in x :
    print(v ** 2) # 4 9 16
p = iter(x)
try :
    while True
        print(next(p) ** 2) # 4 9 16
except StopIteration
    pass


x = [2, 3, 4]
print(x ** 2) # not ok

# print the square of the first element, the cube of the rest of the elements
x = [2, 3, 4, ...] # list
p = iter(x)        # list iterator
print(next(p) ** 2) # 4
try :
    while True
        print(next(p) ** 3) # ...
except StopIteration
    pass

x = [2, 3, 4, ...]  # list
p = iter(x)         # list iterator
print(x is p)       # false
print(next(p) ** 2) # 4

q = iter(p)         # list iterator
print(p is q)       # true

for v in x :        # not right
    print(v ** 3)   # 8, 27, 64

for v in p :
    print(v ** 3)   # 27, 64

x = [2, 3, 4]          # list
y = [v * 5 for v in x] # list comprehension, eager

x = [2, 3, 4]          # list
g = (v * 5 for v in x) # generator, lazy
y = next(g)
print(y)               # [10]
y = next(g)
print(y)               # [15]
y = next(g)
print(y)               # [20]
y = next(g)            # raises StopIteration

x = [2, 3, 4]          # list
g = (v * 5 for v in x) # generator, lazy
for y in g :
    if (...)
        break

x = [] # list
x = () # tuple
x = {} # dict

x = {2, 3, 4}
x = {2: "abc", 3: "def", 4: "ghi"}

x = list()  # empty
x = tuple()
x = str()
x = set()
x = dict()

assert reduce(concat, b, "") == "nothing to be done." # expensive
assert "".join(b)            == "nothing to be done." # much, much cheaper



































