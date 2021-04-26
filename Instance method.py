# instance method is the are the functions in the same class which use the instancess 


class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


    def setdiscount(self, amount):
        self._discount = amount # here the _discount is a secret variable so we can't use it for another class
        
        
    def ifthereis(self):
        if hasattr(self, "_discount"):
            return self.price - self._discount
        else:
            return self.price


b = Book("Origin", "Dan Brown", 400, 500)
print(b.ifthereis())
b.setdiscount(200)
print(b.ifthereis())
print(b.price)

