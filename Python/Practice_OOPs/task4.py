
# Task: Create a class Laptop with brand and price. Change the price after creating the object

class laptop:

    def __init__(self,brand,price):
        self.brand = brand
        self.price = price 

l1 = laptop("Dell",100000)
l1.price = 20000
print("The laptop name is",l1.brand)
print("updated price is",l1.price)        