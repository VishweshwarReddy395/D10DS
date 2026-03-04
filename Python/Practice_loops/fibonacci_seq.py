#  using for LOOPS
n = int(input("Enter the number:"))

a = 0
b = 1
if n == 1:
    print(a)
else: 
    print(a)
    print(b)
    for i in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)


n = int(input("Enter the number:"))
a = 0
b = 1
for i in range(2,n):
    print(a)
    a,b = b,  a+b         #a gets the current value of b , b gets the sum of the current a and b

# using while Loop

n = int(input("Enter the number :"))

a = 0
b = 1 
count = 0
while count<=n:
    print(a)
    a,b = b , a+b
    count += 1