#Pythonprogram to find the factorial of an number


def factorial(num):  
    if num<0:
        print("Sorry there is factorial for negative numbers ")
    elif num==0:
        print("The factorial of 0 is 1 ")
    else:
        fact=1
        for i in range(1,num+1):
            fact*=i
        print("The factorial of %d is" %(fact))
num = int(input("Enter the number:"))
factorial(num)

