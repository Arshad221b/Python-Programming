from abc import ABC, abstractmethod

class INterface: # here we created an interface for the function your_name which gives us an interface, which we can use it later in C
    @abstractmethod   # here, we don't do anything in this class, it's just an interface!
    def your_name(self):
        pass
                 
class A:
    def __init__(self) -> None:
        super().__init__()
        self.address = "address"
    
    @abstractmethod    
    def street(self):
        pass
       
class C(A, INterface):
    def __init__(self) -> None:
        super().__init__()
           
    def your_name(self):
        print("Hakuna Matata")
        
    def street(self):
        print(self.address)
        
        
c = C()
c.your_name()
c.street()