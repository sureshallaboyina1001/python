#sum of all digits of number

num = int(input('enter a number:'))
sum = 0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10

print("Sum of individual digits is",sum)    

