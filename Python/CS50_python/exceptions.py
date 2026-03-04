"""try:
    n=int(input("Input : "))
    print("Integer.")
except ValueError:
    print("not a integer.")"""

try:
    n=int(input("Input : "))
except ValueError:
    print("not a integer.")
else:
     print("Integer.")