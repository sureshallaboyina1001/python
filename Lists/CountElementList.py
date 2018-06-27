#Number of Ocurrenc eof element in th list

lst=[]
print("How many elements:",end="")
n= int(input())
for i in range(n):
    print("Enter the elements:",end="")
    lst.append(int(input()))

print("the original list:",lst)

element=int(input("enter the element:"))

count=0
for i in lst:
    if(element==i):
        count+=1
print("{} is found {} times".format(element,count))
