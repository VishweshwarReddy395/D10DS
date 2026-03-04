class calculator:
    def __init__(self,n):
        self.n = n

    @staticmethod         # To greet , we are using static method which is not a object itself
    def greet():
        print("Welcome to Calculator")

    def sqaure(self):
        print(f"The sqaure is {self.n * self.n}")
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")
    def sqaure_root(self):
        print(f"The sqaure is {self.n ** 1/2}")

a = calculator(6)
a.greet()           # we are greeting using static method
a.sqaure()
a.cube()
a.sqaure_root()



# from random import randint

# class Train:
#      def __init__(self,trainNo):
#           self.trainNo = trainNo
          

#      def book(self,fro,to):
#           print(f"Ticket is booked in train no :{self.trainNo} from {fro} to {to}")
     
#      def getstatus(self):
#           print(f"Train No :{self.trainNo} is running on time")
     
#      def getfare(self,fro,to):
#           print(f"Tickets fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,555)}")

     
# t = Train(12399)
# t.book("rampur","Delhi")
# t.getstatus()
# t.getfare("rampur","Delhi")
