class employee:
    company = "Microsoft"
    def e1(self):
        print(f" the comapny is {self.company}")

class programmer(employee):
     name = "Vishu"
     def n1(self):
         print(f"The name of the programmer is {self.name}")

class manager(programmer):
    role = "Default role"
    def m1(self):
        print(f"The role of the manager is {self.role}")


a = employee()
print(a.company)

a = programmer()
print(a.company,a.name)

a = manager()
print(a.company,a.name,a.role)