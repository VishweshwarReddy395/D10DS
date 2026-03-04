# Problem 1:
# Create a base class Animal with a method speak() that prints "Animal speaks".
# Create a derived class Dog that inherits Animal and calls speak()

class Animal:
    def speak(self):
        print(f"The Animal Speaks")


class Dog(Animal):
    pass


a = Animal()
a = Dog()
a.speak()