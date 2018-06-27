#max and min in the list
lst=[]
print("How many elements:",end='')
n=int(input())


for i in range(n):
    print("Enter the elements:",end="")
    lst.append(int(input()))

print("list=",lst)

max=lst[0]
min=lst[0]

for i in range(1,n):
    if lst[i]>max:
        max=lst[i]
    if lst[i]<min:
        min=lst[i]
print("maximum element=",max)
print("minimum element=",min)
