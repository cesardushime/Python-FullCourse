#mutliple inheritance= when a child class is derived from omore than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal hunts")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.flee()
fish.hunt()