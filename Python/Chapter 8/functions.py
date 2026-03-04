
# Functions can be used to reduce complexity . 
# By writing multiple lines of code we can write a piece of code in a function and we can call it as many times it is required

# Function Definition
def avg():

    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))

    average = (a+b+c)/3

    print(average)

avg()    # Function Call


# Another Example

def fun1():
    print("Hello")


fun1()