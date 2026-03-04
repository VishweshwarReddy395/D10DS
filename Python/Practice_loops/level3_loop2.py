
# 2.Calculate the factorial of a number
# Input: 5 → Output: 120

n = int(input("Enter the number :"))

fact = 1

for i in range(1,n+1):
    fact = fact * i
print(f"Factorial of {n} is {fact} ")