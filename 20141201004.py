#!/usr/bin/env python

# if...elif...else
age = 16
print 'your age is', age
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

# for...in
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name
print 'range(5): ', range(5)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# raw_input()
birth = int(raw_input('birth: '))
if birth < 2000:
    print '< 2000'
else:
    print '>=2000'
