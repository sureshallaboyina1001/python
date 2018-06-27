from abc import *

class Myclass(ABC):
    def connect(self):
        pass
    def disconnect(self):
        pass
class Oracle(Myclass):
    def connect(self):
        print("Connected to Oracle database")
    def disconnect(self):
        print("disconnected to Oracle db")
class MySql(Myclass):
    def connect(self):
        print("Connected to MySQL database")
    def disconnect(self):
        print("disconnected to MySQL db")

str = input("enter the DATABASE name:")

classname=globals()[str]
x=classname()
x.connect()
x.disconnect()
