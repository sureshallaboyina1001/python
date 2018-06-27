# sorting an array using Buuble short tecnique
from array import *
arr = array("i",[])

print("How many ekements?",end="")
n = int(input())
for i in range(n):
    print("enter elements:",end=(''))
    arr.append(int(input()))
print("original array:",arr)


#bubble sort
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            t = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = t
            flag = True
        if flag==False:
            break
        else:
            flag = False

print('sorted array=',arr)