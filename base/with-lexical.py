#!/usr/bin/env Python

'''
file = open("/etc/resolv.conf")
try:
    data = file.read()
finally:
    file.close()


with open("/etc/resolv.conf") as file:
    data = file.read()
    print data
'''

class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, type, value, trace):
        print "In __exit__()"
 
 
def get_sample():
    return Sample()
 
 
with get_sample():
    print "sample:"