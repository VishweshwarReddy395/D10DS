
class demo():
    a = 4


b = demo()
print(b.a)        # Prints the class attribute . because Instance attribute is not present

b.a = 0           # Instance attribute is set
print(b.a)        # prints the instance attribute because instance attribute is present               
