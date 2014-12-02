#!/usr/bin/env python

# List
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print 'len(classmates) = ', len(classmates)
print 'classmates[0]: ', classmates[0]
print 'classmates[-1] ', classmates[-1]
# w+
classmates.append('Adam')
print classmates
# insert
classmates.insert(1, 'Jack')
print classmates
# delete
classmates.pop()
print classmates
classmates.pop(1)
print classmates
# replace
classmates[1] = 'Sarah'
print classmates
# differente data type
L = ['Apple', 123, True]
print L
s = ['python', 'java', ['asp', 'php'], 'scheme']
print s
print 'len(s)', len(s)

# tuple
classmates_tuple = ('Michael', 'Bob', 'Tracy')
t = (1,)
print classmates_tuple, t
