"""# Phone Number

People = {"Vishu":"9010865857","Venki":"97655857","Gindri":"76545857"}

print(len(People))

print(type(People))

People.update({"Kalyan":"4566789","shivani":"987654378"})
print(People)

values=People.values()
print(values)

Key=People.keys()
print(Key)

People.pop("shivani")
print(People)

People.popitem()
print(People)"""


"""People=[{"Name":"Vishu","Number":"90109876"},
        {"Name":"Venki","Number":"90109879"},
        {"Name":"Gindri","Number":"90109870"}
        ]
    

print(type(People))

Name=input("Name : ")
for person in People:
    if person["Name"]==Name:
        Number = person["Number"]
        print(f"Number : {Number}")
        break
else:
    print("Not Found")"""


People = {"Vishu":"9010865857","Venki":"97655857","Gindri":"76545857"}
        
name=input("Name: ")
if name in People:
    print(f"Number: {People[name]}")
else:
    print("Not Found")