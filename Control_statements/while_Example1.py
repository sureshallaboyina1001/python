# to display even number btw 100 to 200

num= int(input("enter a number:"))
if num%2!=0:
    num-=1
while num>=100 and num<=200:
    print(num)
    num+=2
