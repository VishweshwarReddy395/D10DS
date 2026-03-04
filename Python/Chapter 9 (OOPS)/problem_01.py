
class programmers:
    company = "Microsoft"
    
    def __init__(self,name,domain,salary):
        self.name = name
        self.domain = domain
        self.salary = salary
      
        
        
p1 = programmers("Vishweshwar","Cloud computing",30000)
print(p1.name, p1.domain, p1.company, p1.salary)
p2 = programmers("Venki","frontend manager",40000)
print(p2.name, p2.domain, p2.company, p2.salary)