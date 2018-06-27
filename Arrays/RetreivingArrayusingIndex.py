# to retreive the elements in the array using array index

from array import *

arr= array("i",[10,20,34,56,48,1])
n = len(arr)
print("Array using FOR loop")
for i in range(n):
    print(arr[i], end=" ")



print("\narray using while loop")
i=0
while i<n:
    print(arr[i],end=" ")
    i+=1