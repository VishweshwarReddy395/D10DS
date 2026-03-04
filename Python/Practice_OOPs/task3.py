
# Create a class Car with brand and a default value wheels = 4.

class car:


    def __init__(self,brand):
        self.brand = brand 
        self.wheels= 4


c1 = car("Toyota")
print("the car is :",c1.brand)
print("It has ",c1.wheels)