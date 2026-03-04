# Print the multiplication table of a number (e.g., 7)
# Input: 7 → Output: 7 x 1 = 7 ... 7 x 10 = 70

n = int(input("Enter  the number : " ))             # Using for loop
for i in range(1,11):
    print(f"{n}x{i}={n*i}")
   

n = int(input("Enter  the number : " ))           # using while loop
i = 1
while(i<11):
    print(f"{n}x{i}={n*i}")
    i+=1