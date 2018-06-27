#Aliasing of an array

from numpy import *

a= arange(1,6)
b= a
print("original array",a)
print("Aliasing Array",b)

b[1]=23

print("--After Modifiactions--")
print("Array a:",a)
print("Array b:",b)
