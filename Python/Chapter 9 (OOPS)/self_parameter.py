class students:
    name = "rohan"
    attendance = 90.0

    def getInfo(self):
        print(f"The name of the Student is {self.name}.\nThe Attendamce is {self.attendance}")


stud_1 = students()
stud_1.getInfo()
stud_2 = students()
stud_2.name="Jashwanh"
stud_2.getInfo()
stud_3 = students()
stud_3.name="Venkat" 
stud_3.attendance = 65.0
stud_3.getInfo()
