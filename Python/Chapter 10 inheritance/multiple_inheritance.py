
class employee:
    company = "ITC"
    name = "Default name"

    def show(self):
        print(f"The name is {self.name} and the name of the company is {self.company}")

class coder:
    language = "Python"

    def showLanguage(self):
        print(f"The name of the is language is {self.language}")

class programmer(employee,coder):
    company = "ITC InfoTech"
    def showcompany(self):
        print(f"The name of the company is {self.company}")
    
a = employee()
b = coder()
c = programmer()

c.show()
c.showLanguage()
c.showcompany()