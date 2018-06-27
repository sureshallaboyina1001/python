elements = [10,20,0,68,67]
 
x = bytearray(elements)

x[0] = 20
x[3] = 50

for i in x: print(i)