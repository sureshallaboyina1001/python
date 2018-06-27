#slicing An Array

from numpy import *

arr=arange(1,6)
print(arr)

c=arr[::]
print(c)

b=arr[-2:2:-1]
print(b)