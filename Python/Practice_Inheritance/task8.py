# Problem 8:
# Create any base and child class, then use isinstance() and issubclass() to test relationships.

class Animal:

    def speak(self):
        print("The Animal speaks")

class Dog(Animal):

    def bark(self):
        print("Dog Barks")

d = Dog()

print(isinstance(d,Dog))
print(isinstance(d,Animal))
print(isinstance(d,object))
print(issubclass(Dog,Animal))
print(issubclass(Dog,object))
print(issubclass(Animal,Dog))
