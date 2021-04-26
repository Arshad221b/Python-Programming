# class methods are those which are applied to the entire class

class Book:

    BOOK_TYPE = ("HARDCOVER", "PAPERBACK", "COMIC")

    def __init__(self, booktype) -> None:
        if not booktype in Book.BOOK_TYPE:
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


    @classmethod
    def printbook(cls):
        print(cls.BOOK_TYPE)



b = Book("COMIC")
b.printbook()
c = Book("NOVEL")
c.printbook()