class Myclass:
    def __init__(self):
        self.x=4
        self.__y=3

m=Myclass()
print(m.x)
print(m._Myclass__y)
