# model/animal.py

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"