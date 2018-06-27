f=open("file2.txt",'a+')

print("please enter the string:")
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")

f.seek(0,2)
print("The file content:")
str=f.read()
print(str)
f.close()
