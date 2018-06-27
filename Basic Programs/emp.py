from array import*
eno=array('i',[])
ename=array('i',[])
esal=array('i',[])


#call the function
n= int(input('how many employees you want:'))
for i in range(n):
    eno.append(int(input("enter a number:")))
    ename.append(str(input("enter a name:")))
    esal.append(float(input("enter a salary:")))
m= len(eno)
p= len(ename)
q= len(esal)

for i in range(m):
    print(eno[i])
for j in range(p):
    print(ename[i])
for k in range(q):
    print(esal[i])    
 

"""def empid(eno):
    return eno
def empname(ename):
    return ename
def empsal(esal):
    return esal"""
   
"""res=empid(eno)
res1=empname(ename)
res2=empsal(esal)
for a in res:
    print("employee no: ",a)
for b in res1:
    print("employee name: ",b)
for c in res2:
    print("employee sal: ",c)"""