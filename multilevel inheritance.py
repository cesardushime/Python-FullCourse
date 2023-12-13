#multi-level inheritance is when a derived (child) class inhreits another ferived (child) class

class Organism:
    alive = True
class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print("Alive:" + str(dog.alive))
dog.eat()
dog.bark()