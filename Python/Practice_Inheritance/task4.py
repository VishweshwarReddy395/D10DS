# Problem 4:
# Use super() in the Student class to call the constructor of Person and then add the grade.

class Person:

    def __init__(self,name):
        self.name = name 
        print(f"Person Constructor called")


class Student(Person):

    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
        print(f"student constructor called")

class CrStudent(Student):

    def __init__(self, name, age,college):
        super().__init__(name, age)
        self.college = college
        print(f"CrStudent Constructor called")

c = CrStudent("Vishu",21,"IIT")