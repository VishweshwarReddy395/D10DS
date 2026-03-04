# lower = int(input("Enter the number:"))
# upper = int(input("Enter the number:"))

# for i in range(lower,upper +1):
#     if i>1:
#         for num in range(2,i):
#             if i % num ==0:
#                 break

#     else:
#         print(i)



lower = int(input("Enter the limit here:"))
upper = int(input("Enter the limit here:"))

for i in range(lower,upper + 1):
    if i > 1:
        for num in range(2, i):
            if i % num == 0:
                break
        else:
            print(i)