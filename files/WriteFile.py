#to store data into file

f=open("file1.txt",'w')
data=input("Enter the data:")
f.write(data)
f.close()
