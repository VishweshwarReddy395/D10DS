
# Task: Create a class Student and create 3 objects with different data.

class student:

    def __init__(self,Name,Class,rollno):
        self.Name = Name 
        self.Class= Class
        self.rollno = rollno

s1 = student("Vishweshwar","Fourth",22)
print("Student Name is ",s1.Name)
print("Studying in class",s1.Class)
print("Roll No :",s1.rollno)
        
s2 = student("Venki","Fourth",23)
print("Student Name is ",s2.Name)
print("Studying in class",s2.Class)
print("Roll No :",s2.rollno)