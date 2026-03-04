
marks ={
    "Harry":100,
    "Vishu":98,
    "Mani":78
}

print(marks.items())       # Returns all key value pairs from a dictionary

print(marks.keys())        # Returns all key pairs from a dictionary

print(marks.values())      # Returns all value pairs from a dictionary

marks.update({"Harry":66,"Gindri":100}) # update the values for the specified key in the dictionary

print(marks)

print(marks.get("Vishu"))    # returns the values for the specified key in the dictionary

print(marks.get("Venki"))    # Returns None as the key is not available in the dictionary

print(marks.clear())         # removes all elements from the dictionary

v = marks.pop("Harry")       # pop the key and value

print(v)

print(marks)