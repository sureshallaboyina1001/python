#sorting a list without using sort()

lst=[]
print("Hwo many elements:",end='')
n=int(input())

for i in range(n):
    print("Enter element:", end="")
    lst.append(int(input()))

print("Original List:",lst)

flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if lst[j]>lst[j+1]:
            t = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = t
            flag = True
        if flag==False:
            break
        else:
            flag=False
print("sorted list:",lst)
