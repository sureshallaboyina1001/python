import os,sys

fname=input("enter the filename:")
if os.path.isfile(fname):
    print("File exists")
    f=open(fname,'r')
else:
    print("File doesn't exixts:",fname)
    sys.exit()

print("The file content:")
str=f.read()
print(str)
f.close()
