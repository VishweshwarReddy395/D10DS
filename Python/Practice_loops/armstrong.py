n = int(input("enter a number:"))

x = len(str(n))
temp = n
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r ** x
    n = n//10                           

if temp == sum:
    print("It is a Armstrong Number")          # examples are 153,671,1634
else:
    print("It is not a Armstrong Number")