#Inheritance
class Square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print("Area of Square:",self.x*self.x)
class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        super().area()
        print("Area of rectangle",self.x*self.y)
a,b=10,20
r=Rectangle(a,b)
r.area()
