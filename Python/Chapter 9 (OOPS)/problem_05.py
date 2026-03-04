from random import randint

class train:

    def __init__(self,trainNO):
        self.trainNo = trainNO

    def book(self,fro,to):
        print(F"Ticket is booked in the train no {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no {self.trainNo} is running on time")
        
    def getfare(self,fro,to):
        print(f"Ticket is booked in the train no {self.trainNo} from {fro} to {to} is {randint(222,543)}")


t = train(1234)
t.book("Hyderabad","vishakapatnam")
t.getstatus()
t.getfare("Hyderabad","Vishakapatnam")