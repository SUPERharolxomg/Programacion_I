# model/flight.py

from abc import ABC, abstractmethod

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyer):
    def fly(self):
        return "The bird is flying with its wings."

class Airplane(Flyer):
    def fly(self):
        return "The airplane takes off with its engines."