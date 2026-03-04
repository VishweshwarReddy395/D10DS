class calculator:
    def __init__(self,n):
        self.n = n

    def sqaure(self):
        print(f"The sqaure is {self.n * self.n}")
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")
    def sqaure_root(self):
        print(f"The sqaure is {self.n ** 1/2}")

a = calculator(6)
a.sqaure()
a.cube()
a.sqaure_root()
        