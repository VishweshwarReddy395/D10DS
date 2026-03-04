# python program to check whether a number is palindrome or not

# num = int(input("Enter the number :"))

# original = num
# reverse = 0

# while num > 0:
#     r = num % 10                    # by doing this step we get the remainder(r)
#     reverse = reverse * 10 + r      # in this step, initially the reverse is 0 and we multiply with 10 and add with r
#     num = num // 10                 # In this step , the quoitent is divided with floor dividon operator(//) 10 to get the value

# if original == reverse:
#     print(f"is a palindrome number")
# else:
#     print(f"is not a palindrome number")


# python program to check whether a string is palindrome or not

text = input("Enter a string: ")

is_palindrome = True
length = len(text)

for i in range(length // 2):
    if text[i] != text[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")

