
# else statement is used to catch all true values if the IF , ELIF statements are wrong or not satisfied 

a = int(input("Enter your age : "))

if a>18:
     print("eligible to Vote")
elif a<10:
     print("Not ELigible to vote")
else:
     print("still a minor")

