#Inner class example

class Person:
    def __init__(self):
        self.name='charles'

    def display(self):
        print("Name:",self.name)

    class DOB:
        def __init__(self):
            self.dd=10
            self.mm=3
            self.yy=1998
        def display(self):
            print("DOB:{}/{}/{}".format(self.dd,self.mm,self.yy))
p=Person()
p.display()
x=Person().DOB()
x.display()
print(x.yy)
