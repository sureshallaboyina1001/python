#Reverse of number
num = int(input('enter a number'))

rev=0
while num>0:
     rem = num%10
     rev = (rev*10)+rem
     num = num//10
     
print("Reverse of number:",rev)