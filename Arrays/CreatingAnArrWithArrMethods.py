#Creating an Array Using array(),linespace(),logspace(),zeros(),ones(),arange()


from numpy import *

print("Using array method")
arr = array([10,20,20,34],int)
print(arr)


print("Using lineSpace method")
arr = linspace(100,200,10)
print(arr)

print("Using logspace method")
arr = logspace(5,10,3)
print(arr)

print("Using Zeros Method")
arr1 = zeros(5,int)
print(arr1)
arr2 = zeros(3,float)
print(arr2)


print("Using Ones method")
arr = ones(5,int)
print(arr)
arr2 = ones(3,float)
print(arr2)


print("using Arange Method")
arr = arange(1,100,10)
print(arr)
arr2 = arange(100,80,-2)
print(arr2)
