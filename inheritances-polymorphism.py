#!/usr/bin/env python

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

class Dog1(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

a = list()
b = Animal()
c = Dog()

isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)
isinstance(c, Animal)

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())

run_twice(Dog())

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'
run_twice(Tortoise())
