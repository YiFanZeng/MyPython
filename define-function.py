#!/usr/bin/env python

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
age =20
def nop():
    pass
if age >= 18:
    pass
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
