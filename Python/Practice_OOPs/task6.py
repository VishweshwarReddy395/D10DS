# Create a class Rectangle with attributes length and width. Add a method area() that returns the area.

class Rectangle:

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
           return self.length * self.width


r = Rectangle(2,3)
print("Area",r.area())