# to print n to 2 even number

num = int(input('enter a number: '))
 
if num%2!=0:
    num-=1
    while num>=2:
        print(num)
        num-=2
print("{} is even number".format(num))
