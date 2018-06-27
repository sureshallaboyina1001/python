
def elements(name,age,score):
    return name,age,score

for i in range(3):
    name = input("enter name:")
x=[]
lst=x.append(name)
tup = tuple(lst)
    
for i in range(3):
    age = int(input("enter a age:"))
for i in range(3):
    score = int(input("enter a score:"))
    tup1 =(name,age,score)
    print(tup1)
lst=list(tup1)
print(lst)
elements(name,age,score)
