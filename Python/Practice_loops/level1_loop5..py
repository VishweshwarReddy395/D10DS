
#   Print the reverse of a string
# Input: "hello" → Output: "olleh"

text=input("enter the String: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text
print("Reversed:",reversed_text)

# | Iteration | `char` | `reversed_text`        |
# | --------- | ------ | ---------------------- |
# | 1         | `h`    | `h`                    |
# | 2         | `e`    | `e` + `h` = `eh`       |
# | 3         | `l`    | `l` + `eh` = `leh`     |
# | 4         | `l`    | `l` + `leh` = `lleh`   |
# | 5         | `o`    | `o` + `lleh` = `olleh` |



text = input("enter the string:")                      # String Slicing

print("Reversed String:",text[::-1])