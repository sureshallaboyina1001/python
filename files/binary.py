f1=open("dims.jpg",'rb')
f2=open("new.jpg",'wb')

bytes=f1.read()
f2.write(bytes)

f1.close()
f2.close()
