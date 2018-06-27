#multiplication table
num = int(input("enter the number:"))

for i in range(1,21):
    print("{:2d}*{:2d} = {:3d}".format(num,i,num*i))