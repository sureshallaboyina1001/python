#viewing an array using view()


from numpy import *

a = arange(5,10)
b= a.view()

print("Original Array:",a)
print("New Array:",b)
b[0]=11
print("After modifications")
print("Orginal Array:",a)
print("New Array:",b)