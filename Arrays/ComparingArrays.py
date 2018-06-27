#using logical_and(),logical_or(),logical_not()

from numpy import *

arr1=array([1,3,2],int)
arr2=array([1,3,0],int)

arr3 = logical_and(arr1<0,arr1>4)
print(arr3)

arr3 = logical_or(arr2 <0,arr2>4)
print(arr3)