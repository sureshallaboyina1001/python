#BYTES Demo
print("BYTES DEMO")
elements1 = [10,20,30,40]
num1 = bytes(elements1)
for i in num1:
    print(i)

#BYTEARRAY DEMO
print("BYTEARRAY DEMO")
elements2 = [10,20,30,40,50]
num2 = bytearray(elements2)
for k in num2:
    print(k)
num2[2]=34
num2[4]=48
print("ByteArray Changed")
for x in num2:
    print(x)