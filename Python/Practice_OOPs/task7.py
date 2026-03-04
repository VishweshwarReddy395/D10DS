# Task: Create a class Book and a function that takes a Book object and prints its details.

class Book:

    def __init__(self,author,title):
        self.author = author
        self.title = title

    def ShowBookInfo(self):
        print(f"The Author of the book is {self.author}")
        print(f"The Title of the book is {self.title}")


b1 = Book("Valmiki","Ramayana")
b1.ShowBookInfo()
        