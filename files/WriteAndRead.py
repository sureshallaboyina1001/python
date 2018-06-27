f=open("textfile.txt",'w')
print("Enter the string:")
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")

f.close()
