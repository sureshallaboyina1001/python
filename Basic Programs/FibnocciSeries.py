#Fibnocci Series using python

num1=0
num2=1
count=int(input('enter a max number:'))
for i in range(2,count):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3