#abilitity of oop to allow a subclass to use a more specific implementation fo the parent class

class Animal:
    def eat(self):  #defined with the matching signature to the parent class
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()