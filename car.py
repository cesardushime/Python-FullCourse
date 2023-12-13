class Car:  #creating a blueprint for objects by capitalizing it
    wheels = 4 #class variable inside a class, but outside of the constructor
    def __init__(self, make, model, year, color):  #Constructor, or a special method to create object
        self.make = make  #instance variable inside the constructor
        self.model = model #instance variable inside the constructor
        self.year = year  #instance variable inside the constructor
        self.color = color  #instance variable inside the constructor

    def drive(self): #class method for the action of an object
            print("The " +self.model + " is driving!")
    def stop(self):  #class method for the action of an object
            print("The " + self.model + " is stopped")