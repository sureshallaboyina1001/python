class Myclass:
    def __init__(self):
        self.x=4
        self.__y=5
    def display(self):
        print(self.x)
        print(self._Myclass__y)
m=Myclass()
m.display()
print(m.x)
print(m._Myclass__y)
