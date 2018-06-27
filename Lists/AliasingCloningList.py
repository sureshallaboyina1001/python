#Aliasing and Copying of a list


x=[1,3,5,6,7,8]
print("Aliasing")
y=x
print(x)
print(y)
x[1]=2
print(x)
print(y)


print("\n Cloning")
x=[1,3,5,6,7,8]
y=x.copy()
print(x)
print(y)
x[2]=4
y[1]=2
print(x)
print(y)
