# abstract base class (abc) inheritance
from abc import ABC, abstractmethod

class areaof(ABC): # abc is a base class
    def __init__(self, ) -> None:
        super().__init__()
        
    @abstractmethod  # abstractmethod decorator for abstract function, there's no implimentaion in base class but it has to be override in subclasses
    def calcArea(self):
        pass
    
class Circle(areaof):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def calcArea(self):
        return 3.14 * self.radius ** 2
    
    
class Square(areaof):
    def __init__(self, side) -> None:
        self.side = side
        
    def calcArea(self):
        return self.side ** 2
    

c = Circle(4)
s = Square(4)

print(c.calcArea())
print(s.calcArea())    
    
