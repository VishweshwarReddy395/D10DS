class employee:
    language = "python"    # This is a class attribute
    salary = 90000
    Address = "Hyderabad"

employee1 = employee()
employee1.name = "Vishweshwar"
print(employee1.name,employee1.language,employee1.salary,employee1.Address)

employee2 = employee()
employee2.name = "Jashwanth"
employee2.language = "Java Script"         # This is a Insatnce Attribute.It takes over the class attribute
print(employee2.name,employee2.language,employee2.salary,employee2.Address)