class employee:
    a = 1
    def __init__(self):
        print("Constructor of the employee")

class programmer(employee):
    b = 1
    def __init__(self):
        print("Constructor of the programmer")


class manager(programmer):
    c = 1
    def __init__(self):
        super().__init__()
        print("Constructor of the manager")

# o = employee()
# print(o.a)
# o = programmer()
# print(o.b)
o = manager()
print(o.c)


