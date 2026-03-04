class maths:

    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    def __sub__(self,num):
        return self.n - num.n
    def __mu1__(self,num):
        return self.n * num.n

a=maths(2)
b=maths(2)

print(a + b)
print(a - b)
# print(a * b)