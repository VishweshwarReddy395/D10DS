

class Employee:
    company = "Microsoft"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class programmer(Employee):
    company = "Microsoft Excel"
    def showlanguage (self):
        print(f"The name is {self.name} and the language is {self.language}")



a = Employee()
b = programmer()

print(a.company)
print(b.company)

