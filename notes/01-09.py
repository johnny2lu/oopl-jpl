# -----------
# Tue, 09 Dec
# -----------

"""
math problem that's about 80 years old

Collatz Conjecture

take a pos int
if even divide it by 2
otherwise multiply it by 3 and add 1
repeat until 1
"""

5 16 8 4 2 1

"""
cycle length of 5 is 6
cycle length of 10 is 7
"""

"""
/  is true division
// is floor division

with true  division the result is always a float
with floor division the result is the type of the input
"""

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

"""
python exhibits "duck" typing
"""

"""
assertions good for preconditions and postconditions

assertions not good for tests, because first failure results in the rest of the tests not running

assertions not good for protecting against user error
"""

class A :
    def f (self) :
        print("A.f")

x = 2
y = x + 1
print(x)       # 2
print(type(x)) # int
print(isinstance(x, int)) # true

x = "abc"
print(x)       # "abc"
print(type(x)) # str

x = 2.34
print(x)       # 2.34
print(type(x)) # float

x = A()
print(x)       # <address>
print(type(x)) # A

x.f()          # A.f

"""
this exercise is an example of something obvious
and that is that BAD tests can hide BAD code
"""

"""
1. run as is, and confirm the success
2. fix the tests
3. run it again, and confirm the failure
4. fix the code
5. run it again, and confirm the success
"""

"""
assume we don't have exceptions
"""

# return stmt

def f (...) :
    ...
    if (<something wrong>) :
        return -1
    ...

def g (...) :
    ...
    x = f(...)
    if (x == -1) :
        <something wrong>

...
...g(...)...
...

# global variable

h = 0

def f (...) :
    global h
    ...
    if (<something wrong>) :
        h = -1
        return ...
    ...

def g (...) :
    global h
    ...
    h = 0
    x = f(...)
    if (h == -1) :
        <something wrong>

...
...g(...)...
...

# mimic pass by reference

def f (..., e2) :
    ...
    if (<something wrong>) :
        e2[0] = -1
        return ...
    ...

def g (...) :
    ...
    e = [0]
    x = f(..., e)
    if (e == [-1]) :
        <something wrong>

...
...g(...)...
...

# exceptions

def f (...) :
    ...
    if (<something wrong>) :
        raise X()
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except E as e :
        <something wrong>
    ...

...
...g(...)...
...

def f (a, b, c) :
    ...

class A :
    def f (self) :
        self.i = 0

x = A()
print(type(x)) # A

print(x.i)     # <fail>

x.f()

print(x.i)     # 0

x = [2, 3, 4]
print(x)       # [2, 3, 4]
print(type(x)) # list

x = (2, 3, 4)
print(x)       # (2, 3, 4)
print(type(x)) # tuple

"""
tuples are immutable
can't change the size
can't change the content
"""

x = [2]
print(x)       # [2]
print(type(x)) # list

x = []
print(x)       # []
print(type(x)) # list

x = (2)
print(x)       # 2
print(type(x)) # int

x = (2,)
print(x)       # (2,)
print(type(x)) # tuple

x = ()
print(x)       # ()
print(type(x)) # tuple

x = [2, 3, 4]
y = [2, 3, 4]
print(x == y) # true
print(x is y) # false

x = [2, 3, 4]
y = x
print(x is y) # true

"""
is is about identity
== is about content
"""

# exceptions

def f (...) :
    ...
    if (<something wrong>) :
        raise ChildOfE()
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except ChildOfE as e :
        <something wrong>
    except E as e :
        <something wrong>
    ...

...
...g(...)...
...

x = [2, 3, 4]
print(type(x))    # list
print(type(list)) # type
print(type(type)) # type

class A :
    ...

x = A()

x = [2, 2, 2]
print(len(x)) # 3

x = (2, 2, 2)
print(len(x)) # 3

x = {2, 2, 2}
print(x)      # {2}
print(len(x)) # 1

"""
reasonable implementation for a list or tuple
an array that is front loaded
inserting in the array is amortized constant time
index the array in constant time
"""

x =  [2, 3, 4]
x += [5]
print(x)       # [2, 3, 4, 5]

"""
reasonable implementation for a set or frozenset
array is no good, because insertion would always be linear
as I have to search the entire for the array for the element

two classical implementations
1. binary search tree (e.x. red black)
    inserting in the array is log time

2. hashtable
    inserting in the array is amortized constant time
"""

x    = [2, 3, 4] # list
x[1] = 5
print(x)         # [2, 5, 4]

x    = (2, 3, 4) # tuple
x[1] = 5         # <fails>
print(x)         # (2, 3, 4)

x    = {2, 3, 4} # set
x[1] = 5
print(x)         #

x  = [2, 3, 4]
x += 4
print(x)         # [2, 3, 4, 4]

x  = {2, 3, 4}
x |= {5}
print(x)         # {2, 3, 4, 5}

x  = {2, 3, 4}
x |= {4}
print(x)         # {2, 3, 4}

x = {2, 3, 4}
print(type(x))   # set

x = {2: "abc", 3: "def", 4: "ghi"}
print(type(x)    # dict

"""
reasonable implementation for a deque
a doubly-linked list
you can't index the deque, because would be linear time
"""

def f (g, x) :
    return g(x) + g(x)

def addone (v) :
    return v + 1

w = 2

x = f(addone, w)
print(x)         # 6

x = f(lambda v : v + 1, 2)
print(x)         # 6

class A :
    def f (self) :
        ...

x = A() # default constructor
x.f()

i = 2
j = 3
k = i + j
print(k)  # 5

i + j # not ok, expression

f(i + j)

k = 2 + 3
print(k)  # 5

(i + j) = k # not ok, because + returns an rvalue

i = 2 # i is an lvalue
2 = i # not ok, 2 is rvalue

i = j

# + takes two rvalues and returns an rvalue

i = 2
j = 3
i += j # in-place addition, a statement

i += 2
3 += 2 # not ok

k = (i += j) # not ok,

# expression are part of something bigger
# statements stand alone

# functions that take or return functions are called higher-order functions
