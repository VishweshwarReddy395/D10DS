# Problem 6:
# MUltiLevel Inheritance
# Create three classes: Animal → Mammal → Human.
# Each class should have a show_info() method. Call it from a Human object and see the effect.


# Base class
class Animal:
    def show_info(self):
        print("I am an Animal")

# Intermediate class
class Mammal(Animal):
    def show_info(self):
        super().show_info()
        print("I am a Mammal")

# Derived class
class Human(Mammal):
    def show_info(self):
        super().show_info()
        print("I am a Human")

# Create object of Human class
h = Human()
h.show_info()

