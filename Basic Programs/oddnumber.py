#to print odd number from n to 1
num = int(input('enter a number:'))

if num%2==0:
    num-=1
    while num>=1:
        print(num)
        num-=2
        