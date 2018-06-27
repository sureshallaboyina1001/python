#to check the given is ARMSTRONG or not

num = int(input('Enter a number:'))

sum=0
temp=num
while num>0:
    rem = num%10
    sum+=(rem*rem*rem)
    num//=10
if(temp==sum):
    print(temp,"is amstrong number")
else:
    print(temp,"is not a amstrong number")