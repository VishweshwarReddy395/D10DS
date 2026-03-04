# problem 7:
# Hierarchical Inheritance
# Create a class Shape. Inherit from it to create Rectangle and Circle classes.
# Each should have a method to calculate area

import math

class Shape:

    def __init__(self,name):
        self.name = name

    def describe(self):
        print(f"The name of the Shape is {self.name}")

class Rectangle(Shape):

    def __init__(self,length ,width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
class Circle(Shape):

    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius
    
a = Rectangle(10,7)
a.describe()
print("Area",a.area())
a = Circle(7)
a.describe()
print("Area",round(a.area(),2))