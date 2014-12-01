#!/usr/bin/env python

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# dictionary
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']
d['Adam'] = 67
print d
d.get('Thomas', -1)
d.pop('Bob')
print d

# set
s = set([1, 2, 3])
print s
s = set([1, 1, 2, 2, 3, 3])
print s
s.add(4)
print s
s.remove(4)
print s
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

a = ['c', 'b', 'a']
a.sort()
print a
a = 'abc'
a.replace('a', 'A')
print a
b = a.replace('a', 'A')
print b
