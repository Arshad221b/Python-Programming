#inheritance is a concept where the child class gets inherited from the parent class


class specifications:
    def __init__(self, milage, width, length) -> None:
        self.milage = milage
        self.width = width
        self.length = length

class car(specifications): # passing specification to functions
    def __init__(self, wheels, doors, milage, length, width) -> None:
        super().__init__(milage, width, length) # inherited from the super class specification
        self.wheels = wheels
        self.doors = doors
        # self.milage = milage
        # self. length = length
        # self.width = width
        
class bike(specifications): # passing specification to functions
    def __init__(self, wheels, milage, length, width) -> None:
        super().__init__(milage, width, length) # inherited from the super class specification
        self.wheels = wheels
        # self.milage = milage
        # self.length = length
        # self.width = width
        
## as you can see there are milage, length, width which are getting repeated, we can create a super class for this 

c = car(4, 4, 20, 600, 330)
b = bike(2, 60, 300, 75)


print(c.doors)
print(b.length)    