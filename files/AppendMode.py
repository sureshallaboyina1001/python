f=open("textfile.txt",'a+')
print("Enter the strings to be appaend")
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")
f.seek(12,0)
print("The File content are:")
str=f.read()
print(str)
