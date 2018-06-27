#to print the string in forward and reverser order

str = input("Enter the string:")
n = len(str)
i=0
	
while i<n:
    print(str[i],end=" ")
    i+=1
print()


#access the string in reverse order
i=-1
while i>=-n:
    print(str[i],end=" ")
    i-=1

#another a way
i=1
while i<=n:
    print(str[-i],end=" ")
    i+=1