# Count how many times an item occurs in a list
# Input: [1,2,3,2,2,4], item = 2 → Output: 3

list = [1,2,3,2,2,4] 
count = 0
for i in list:
    if i==2:
        count+=1
print("count of 2 is",count)