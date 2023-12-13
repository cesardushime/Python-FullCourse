#Duck typing = concepth where the class of an object is less important than the methods
#Class type is not checked if minimum mthods/attributes are present
#"If it walks like a duck, and it quacks lik a duck, then it must be a duck

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken) #chicken has walk and talk method similar to a duck, then the class type checking