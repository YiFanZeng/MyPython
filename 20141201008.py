#!/usr/bin/env python

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print 'power(4): ', power(4)
print 'power(2, 3)', power(2, 3)

def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city
enroll('Sarah', 'F')

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)
