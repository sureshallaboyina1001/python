#Abstract class Demo

from abc import *

class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
class subclass1(Myclass):
    def calculate(self,x):
        print("Square =",x*x)
import math
class subclass2(Myclass):
    def calculate(self,x):
        print("Square Root=",math.sqrt(x))

obj=subclass1()
obj.calculate(2)

obj2=subclass2()
obj2.calculate(3)
    
