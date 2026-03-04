
class employee:
    name = "harry"
    language = "Python"

    def __init__(self,name,language):       # Dunder Methods
        self.name = name 
        self.language = language 
        # print("the details of the employee")
        

a= employee("harry","python")
print(a.name,a.language)

b= employee("Vishu","Java Script")
print(b.name,b.language)

c= employee("Venkat","Django")
print(c.name,c.language)
