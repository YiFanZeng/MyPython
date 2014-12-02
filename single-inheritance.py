#!/usr/bin/env python

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixin(object):
    def run(self):
        print('Running...')

class FlyableMixin(object):
    def fly(self):
        print('Flying...')
class CarnivorousMixin:
    def carnivorous(self):
        print('Carnivorous...')
class HerbivoresMixin:
    def herbivores(self):
        print('Herbivores...')

class Dog(Mammal, RunnableMixin, CarnivorousMixin):
    pass
