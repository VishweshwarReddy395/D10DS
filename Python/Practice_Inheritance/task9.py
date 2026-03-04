# Problem 9:Protected and Private Members
# Create a base class with a protected (_var) and a private (__var) variable.
# Try accessing them from a child class.

class Parent:

    def __init__(self):
        self.__secret = "hidden from Child"

    def show_secret(self):
        print(self.__secret)


class Child(Parent):
    def __init__(self):
        super().__init__()
        # print(self.__secret)                                 

p = Parent()
p.show_secret()       