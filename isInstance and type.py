# is instance is used to understand if the istance is of given class
# type is used to understand type 


class Book():
    def __init__(self, title):
        self.title = title

    

class Newspaper:
    def __init__(self, headline):
        self.headline= headline


b = Book("Origin")
n = Newspaper("Sakaal")

print(type(b)) # to check the type of instance 
print(type(b) == type(n)) # to check two instances together

print("--"*20)
print(isinstance(n, Book)) # to check if n is instance of Book

# <class '__main__.Book'>
# False
# ----------------------------------------
# False