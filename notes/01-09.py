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






























