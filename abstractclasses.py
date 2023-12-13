#Abstract classes prevent user from creating an object of that class
# Contains one or more abstract methods
# Abstract method; it a method declared but not implemented

from abc import ABC, abstractmethod
class Vehicle(ABC): #Abstract class
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("YOu drive the car")
    def stop(self):
        print("This car is stopped")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride a motocycle")
    def stop(self):
        print("This motocycle is stopped")
car = Car()
motorcycle = Motorcycle()

car.go()
car.stop()
motorcycle.go()
motorcycle.stop()