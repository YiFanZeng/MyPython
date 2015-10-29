#!/usr/bin/env python

# sorted()
sorted([36, 5, 12, 9, 21])

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
sorted([36, 5, 12, 9, 21], reversed_cmp)

sorted(['about', 'bob', 'Zoo', 'Credit'])

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)

# return
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
f()

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1()
print f2()
