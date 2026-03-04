# class parent:
#     skill1 = "writing"
#     def write(self):
#         print(f"The skills belonging to parent is {self.skill1}")

# class child(parent):
#     skill2 = "reading"
#     def read(self):
#         print(f"The skills belongin to the child is {self.skill1} and {self.skill2}")

# a = parent()
# a.write()
# a = child()
# a.write()
# a.read()


# class Grandparent:
#     skill = "writing"
#     def write(self):
#         print(f"He is best at {self.skill}")

# class parent:
#     skill1 = "reading"
#     def read(self):
#         print(f"He is best at {self.skill1}")

# class child(Grandparent,parent):
#     skill2 = "listening"
#     def listen(self):
#         print(f"he is best at {self.skill},{self.skill1} and {self.skill2}")


# a = Grandparent()
# a.write()
# a = parent()
# a.read()
# a = child()
# a.write()
# a.read()
# a.listen()

# class Grandparent:
#     skill = "writing"
#     def write(self):
#         print(f"He is best at {self.skill}")

# class parent(Grandparent):
#     skill1 = "reading"
#     def read(self):
#         print(f"He is best at both {self.skill} and {self.skill1}")

# class child(parent):
#     skill2 = "listening"
#     def listen(self):
#         print(f"he is best at {self.skill},{self.skill1} and {self.skill2}")


# a = Grandparent()
# a.write()
# a = parent()
# a.read()
# a = child()
# a.listen()

class Grandparent:
    skill = "writing"
    def __init__(self):
        print("He is a good Boy")

    def write(self):
        print(f"He is best at {self.skill}")

class parent(Grandparent):
    skill1 = "reading"
    def __init__(self):
        print("she is a good gir1")
    def read(self):
        print(f"He is best at both {self.skill} and {self.skill1}")

class child(parent):
    skill2 = "listening"
    def __init__(self):
        super().__init__()
    def listen(self):
        print(f"she is best at {self.skill},{self.skill1} and {self.skill2}")


a = Grandparent()
a.write()
a = parent()
a.read()
a = child()
a.listen()



