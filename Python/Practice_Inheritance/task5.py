# Problem 4:
# Create a Vehicle class.
# Inherit from it to create Car and Bike classes with their own describe() methods


class vehicle:
    
    def __init__(self,brand):
        self.brand = brand

    def show(self):
        print(f"The Vehicle has {self.brand}")


class car(vehicle):

    def describe(self):
        print(f"The car brand is {self.brand}")


class Bike(vehicle):

    def describe(self):
        print(f"The Bike brand is {self.brand}")

v = car("toyota")
v.describe()
v = Bike("yamaha")
v.describe()



    