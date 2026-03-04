
# Task: Add a method greet() to the Person class that prints a greeting using the person's name.


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Bob")
p1.greet()


          