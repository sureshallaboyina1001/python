#Insert Element in Tuple

x=(10,45,45,34,56,60)
print(x)

lst=[int(input("Enter the new element:"))]

new=tuple(lst)

pos=int(input("Enter position no:"))

y=x[0:pos-1]
y =y+new
x=y+x[pos-1:]
print(x)
