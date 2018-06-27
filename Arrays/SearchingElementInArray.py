#search an element in array
from array import *

arr = array('i',[])

print("How many elements?:",end="")
n = int(input())

for i in range(n):
    print("enter elements:",end=" ")
    arr.append(int(input()))

print('Orginal Array:', arr)
print("enter the element to be searched:", end=' ')
s = int(input())

flag=False
for j in range(len(arr)):
    if s==arr[j]:
        print("found the position:",j+1)
    flag=True
if flag==False:
    print("not found the element")
       