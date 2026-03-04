# for i in range(4):

#     for j in range(4):
#         print("*",end = "")

#     print()


# Increasing Triangle 

# def pattern(n):

#     for i in range(n):
#         for j in range(i+1):
#             print("*",end="")
        
#         print()

# pattern(5)


# # Decreasing Triangle 

# def pattern(n):

#     for i in range(n):
#         for j in range(i,n):             # prints from i to n which is 5 . if i = 0 , then we print from 0 to 4 and so on...
#             print("*",end="")
        
#         print()

# pattern(5)

# Right sided Triangle

# n = int(input("Enter the number:"))

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end = " ")

#     print()

# Right sided Downward Triangle

# n = int(input("Enter the number:"))

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = " ")
#     for j in range(i,n):
#         print("*",end=" ")

#     print()


# Hill pattern

# n = 5

# for i in range(n):
#     for j in range(i,n):
#         print(" ",end =" ")
#     for j in range(i):
#         print("*",end =" ")
#     for j in range(i+1):
#         print("*",end =" ")

#     print()


# Down hill pattern

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end =" ")
#     for j in range(i,n-1):
#         print("*",end =" ")
#     for j in range(i,n):
#         print("*",end =" ")

#     print()

n = 5

for i in range(n-1):
    for j in range(i,n):
        print(" ",end =" ")
    for j in range(i):
        print("*",end =" ")
    for j in range(i+1):
        print("*",end =" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
        