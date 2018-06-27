def prime(num):
    if num>1:
        for i in range(2,num):
            if num%2==0:
                print(num,"is not prime no")
                break
        else:
            print(num,"is a prime no")
                



num= int(input("enter the number:"))
prime(num)
