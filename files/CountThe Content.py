import os,sys

fname=input("Enter the file name:")
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    priny("File doesnot exits:")
    sys.exit()

countLine=0
countword=0
countChar=0
for line in f:
    print(line)
    words=line.split()
    print(words)
    countLine+=1
    countword+=len(words)
    countChar+=len(line)
print("no .of lines",countLine)
print("no .of words",countword)
print("no of char",countChar)

f.close()
    
