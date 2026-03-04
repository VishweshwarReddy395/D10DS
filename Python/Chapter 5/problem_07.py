
# same problem like 6th one but in this case both keys must be same and record the output and the value will be updated with the last entered one 
# Check output for a better clarity. later or last entered same value of the key will be updated
# hence it cannot have same keys it would be difficult to work with


d = {}

name = input("Enter the name : ")
language = input("Enter the language : ")
d.update({name:language})
name = input("Enter the name : ")
language = input("Enter the language : ")
d.update({name:language})
name = input("Enter the name : ")
language = input("Enter the language : ")
d.update({name:language})
name = input("Enter the name : ")
language = input("Enter the language : ")
d.update({name:language})

print(d)