#modifying element in tuple

num=(10,20,30,40,50,60)
print(num)

lst=[int(input("Enter the element:"))]
new = tuple(lst)
pos=int(input("Enter Position no"))


num1=num[0:pos]
num1=num1+new
num=num1+num[pos:]
print(num)
