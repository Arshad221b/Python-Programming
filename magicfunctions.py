# string and rper are the two magic functions

class Book:
    def __init__(self, name, author, pages, price) -> None:
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price
        
    #We can use this function for string formatting and debugging
    def __str__(self) -> str:
        return f"{self.name} by {self.author} with {self.pages} pages and price would be {self.price}"
    
    # We can use this function for object representation
    def __repr__(self) -> str:
        return f"title = {self.name}, author = {self.author}, page count = {self.pages}, price = {self.price}"
    
    
    
b = Book("Origin", "Dan Brown", 650, 700)
print(b.__str__())
print(b.__repr__())