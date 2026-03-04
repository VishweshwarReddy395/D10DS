# the values can be same for many keys but the key should be unique. Hence it can same values

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