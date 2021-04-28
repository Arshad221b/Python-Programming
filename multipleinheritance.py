# In python we can use mutiple inheritance 

class A:
    def __init__(self) -> None:
        super().__init__()
        self.mike = "Mike"
        self.name = "Class A"
        
class B:
    def __init__(self) -> None:
        super().__init__()
        self.bob = "bob"
        self.name = "Class B"


class C(A, B): # multiple inheritance
    def __init__(self) -> None:
        super().__init__()
    
    def multiinherit(self):
        print(self.mike)
        print(self.bob)
        print(self.name) # it will print Class A because the class A is passed before B to class C, would print Class B if we pass C(B, A)
        
        
c = C()
print(c.multiinherit())
print(C.__mro__) # method resolution order