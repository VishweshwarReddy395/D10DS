#  Level 3: Logic-based Loops
# 1. Check if a number is prime

# n = int(input("Enter the number:"))

# if n<=1:
#     print("Not a Prime Number")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print(f" {n} is not a prime number ")
#             break
#     else:
#         print(f"{n} is a Prime Number") 


# number = int(input("Enter the number :"))

# for i in range(2,number):
#     if number % i == 0:
#         print("Not a Prime Number")
#         break
# else:
#     print("Prime Number")


# for printing in a range of intervals

lower = int(input("Enter the limit here:"))
upper = int(input("Enter the limit here:"))

for i in range(lower,upper + 1):
    if i > 1:
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            print(i)