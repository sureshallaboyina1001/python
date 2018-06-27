#multi dimensional array

from numpy import *

arr  = array([[1,2,3,5,6],[4,5,6,6,7],[7,8,9,8,10]])

b = arr[1:2,1:2]
c = arr[0:2,0:3]
print(b)
print(c)