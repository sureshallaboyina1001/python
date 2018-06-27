from numpy import *
import sys
r1,c1 = [int(a) for a in input("enter no of rows and colums:").split()]
r2,c2= [int(a) for a in input("enter no of rows and colums:").split()]
if c1!=r2:
    print("Cannot do Multiplication")
    sys.exit()
str1 = input("Enter the elements of a:\n")
m1 =reshape(matrix(str1),(r1,c1))
print("matrix 1:",m1)
str2 = input("Enter the elements of b:\n")
m2 =reshape(matrix(str2),(r2,c2))
print("matrix 2:",m2)

m3 =m1*m2
print("product of M1*M2:\n:",m3)