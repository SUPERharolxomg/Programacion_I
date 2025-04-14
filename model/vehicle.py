# model/vehicle.py

class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        return f" Accelerating... Current speed: {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, brand, model, year, engine):
        super().__init__()
        self.__brand = brand  # Encapsulation
        self.__model = model
        self.year = year
        self.engine = engine  # Composition

    def describe(self):
        return f"{self.__brand} {self.__model} ({self.year}) with a {self.engine.type} engine of {self.engine.power}HP"

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def accelerate(self):
        self.speed += 20
        if self.speed > 200:
            raise OverspeedException(" Excessive speed!")
        return f" Car accelerating... Speed: {self.speed} km/h"

class Bicycle(Vehicle):
    def accelerate(self):
        self.speed += 5
        return f"🚴 Bicycle accelerating... Speed: {self.speed} km/h"

class Engine:
    def __init__(self, type, power):
        self.type = type
        self.power = power

class OverspeedException(Exception):
    pass