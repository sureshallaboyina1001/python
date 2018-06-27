# creating One ARRAY from Another ARRAY

from array import *

arr = array('i',[1,2,3,4])

arr1 = array(arr.typecode,(a*2 for a in arr))
print("the array two elements are:")
for i in arr1:
    print(i,end=" ")
