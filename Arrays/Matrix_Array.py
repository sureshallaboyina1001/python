#Matrices
from numpy import *


arr = array([[1,23,24],[5,6,7]])
arr2 = matrix(arr)
print(arr2)


str ='1,2;3,4;5,6'
a=matrix(str)
print(a)

a=matrix("1,1,3;5,6,7;7,8,9")
print(a)
d = diagonal(a)
print(d)

max_no=a.max()
print("max no is :",max_no)

min_no=a.min()
print("min no is :",min_no)