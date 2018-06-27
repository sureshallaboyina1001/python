#Atributes of an array are ndim,shape,itemsize,size,dtype,nbytes,reshape,flatten
from numpy import *

print("using ndim")
arr = array([[1,1,6,7],[5,6,7,8],[91,56,45,89]])
print(arr.ndim)

print("using shape")
arr=array([[1,2,3],[1,0,9]])
print(arr.shape)

print("using size")
arr= array([[1,2,3],[1,0,9],[9,8,7]])
print(arr.size)

print("using itemsize")
arr= array([1,2,3])
print(arr.itemsize)

print("using dtype")
arr= array([[1,2,3],[1,0,9],[9,8,7]])
print(arr.dtype)

print("using reshape")
arr=arange(8)
arr2 = arr.reshape(4,2)
print(arr2)


print("using nbytes")
arr= array([[1.1,2.1,3.3],[1.4,0,9],[9.9,8.8,7.9]])
print(arr.nbytes)

print("using flatten")
arr= array([[1.1,2.1,3.3],[1.4,0.9,9.8],[9.9,8.8,7.9]])
arr2=arr.flatten()
print(arr2)