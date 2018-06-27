#Copying an array using copy()

from numpy import *

a = arange(11,15)
b= a.copy()
print("Original Array:",a)
print("New Array:",b)
a[1]=20

print("After modifications")
print("Orginal Array:",a)
print("New Array:",b)