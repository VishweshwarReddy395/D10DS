
# Task: Create a class Person with attributes name and age. Create an object and print its attributes.

class Person:
    
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

p1 = Person("Vishweshwar",21)
print("Name:",p1.name)
print("Age:",p1.age)