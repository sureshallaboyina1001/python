class Student:

    def setName(self,name):
        self.name=name

    def setAge(self,age):
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

s=Student()

name=input("Enter the name:")
s.setName(name)
age=int(input("enter age:"))
s.setAge(age)

print("Hi!i'm",s.getName())
print("I'm ",s.getAge(),"old")
