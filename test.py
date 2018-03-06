#!/usr/bin/env python
# -*- coding: utf-8 -*-

'test module'

__author__ = 'niubin'

def f(s):
    return s[0].upper() + s[1:].lower()
print map(f, ['adam', 'LISA', 'barT'])
def prod(l):
    def f(x, y):
        return x * y
    return reduce(f,l)

print prod([1,2,3,4])
import math
def prime(a):
    if a == 1:
        return True
    if a == 2:
        return True
    if not a % 2:
        return False
    else:
        for i in range(2,int(math.sqrt(a)) + 1):
            if not (a % i):
                return False

        return True
def test():
    print("hello world")
d = {}
l = []
d["first"] = l.append(test())

print d
print prime(12)
l = range(1,101)
print filter(prime,l)