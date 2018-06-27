# transpose MAtrix

from numpy import *

r,c=[int(a)for a in input("enter rows and columns:").split()]

str= input("Enter the number:\n")
x = reshape(matrix(str),(r,c))
print("Orginal Array")
print(x)
y=x.transpose()
print(y)

z=y.getT()
print(z)