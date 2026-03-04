class employee:
    company = "ITC"

    @classmethod                     # Prints the class attribute instead of Instance attribute 

    def show(cls):
        print(f"The name of the company is {cls.company}")


a = employee()

a.company = "ITC Infotech"           # Doesnot print Instance attribute

a.show()