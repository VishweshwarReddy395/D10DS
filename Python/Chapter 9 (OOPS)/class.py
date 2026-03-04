
class employee:
    # class attributes
    language="Python"
    salary=9000

a = employee()
a.name="vishu"
print(a.name,a.language)
print(a.salary)

b = employee()
b.name="Venki"                  # name is a instance attribute
print(b.name,b.language)
print(b.salary)