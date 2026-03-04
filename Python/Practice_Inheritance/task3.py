# Problem 3:
# Create a Person class with attributes name and age.
# Create a Student class that inherits from Person and adds grade.


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def show(self):
        print(f"The name of the person is {self.name} and age is {self.age}")

class Student(Person):

    def __init__(self, name, age,grade):
        super().__init__(name, age)
        self.grade = grade 

    def show(self):
        print(f"The name of the person is {self.name} and age is {self.age} and Grade is {self.grade}")



p = Student("Vishu",21,90)
p.show()