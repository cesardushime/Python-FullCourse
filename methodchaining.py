#method chaining = calling multiple methods sequentially
# each call perfomrs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("Your turn off the engine ")
        return self
    def get_out(self):
        print("You step out of the car")
        return self


car = Car()

#car.turn_on()
#car.drive()
#car.brake()
#car.turn_off()

car = Car()
car.turn_on().drive().brake().turn_off().get_out()