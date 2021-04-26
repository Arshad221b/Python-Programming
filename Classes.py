# Python is an object oriented programming language 
# so we have to initialise an object before doing anything 

# class in python

# class Book:
#     pass
# this is an valid class as its not taking any input we don't have to pass any brackets to it like Book()
# but to make it valid we can use pass 

class Book:
    def __init__(self, title):
        self.title = title # here we have created title varible of an object self

# make it inittialise

s = Book("Charlie Sheen") # Here, I'm creating s as a object (self) and then im using to call to print the damn thing 
print(s.title)

print(s)