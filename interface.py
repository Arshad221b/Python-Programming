from abc import ABC, abstractmethod

class INterface:
    @abstractmethod
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