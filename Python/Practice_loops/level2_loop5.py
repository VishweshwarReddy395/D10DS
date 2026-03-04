
# Find the largest number in a list without using max()


numbers = [1,2,3,4,10,1100,1000,9980,98877655]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("largest number is ",largest)