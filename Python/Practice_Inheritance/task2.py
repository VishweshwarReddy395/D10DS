# Problem 2:
# In the Dog class (inherited from Animal), override the speak() method to print "Dog barks".

class Animal:
    def speak(self):
        print(f"The Animal Speaks")


class Dog(Animal):
    def bark(self):
        print(f"the Dog barks")

a = Animal()
a = Dog()
a.bark()