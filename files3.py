import os,sys

fname=input("Enter the filename:")
if os.path.isfile(fname):
    f=open(fname, 'r')
else:
    print(fname+ "does not exists")
    sys.exit()
str=f.read()
print(str)
f.close()