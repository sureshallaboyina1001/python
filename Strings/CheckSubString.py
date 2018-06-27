#Check the string present in the given string or not

str = input("enter the string:")
str2 = input("Enter the sub string:")
if str2 in str:
    print(str2 +" is found")
else:
    print(str2 +" not found")