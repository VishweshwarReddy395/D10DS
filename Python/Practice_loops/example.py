# Print all numbers divisible by 3 from 1 to 100
# i = 1
# count = 0
# while i < 101:
#     if i % 3 == 0:
#         print(f"{i} is divisible by 3")
#         count +=1
#     i +=1

# print(f"Total numbers divisible by 3 is {count}")

# Write a program to count vowels in a string using a loop
# Input: "banana" → Output: 3

# string = input("Enter the string:")

# vowels = "aeiouAEIOU"

# count = 0

# for char in string:
#     if char in vowels:
#         count += 1
    
# print(f"Number of Vowels in the String is {count}")


string = input("Enter the string:")

vowels = "aeiouAEIOU"

# using While Loop

text = input("Enter the string:")

vowels = "aeiouAEIOU"

i = 0

count = 0

while i < len(text):
    if text[i] in vowels:
        count += 1
    i+=1

print(f"Number of Voowels in the Text is {count}")