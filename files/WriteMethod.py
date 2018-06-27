f=open("file2.txt",'w')

print("please enter the strin:")
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str+"\n")
f.close()
