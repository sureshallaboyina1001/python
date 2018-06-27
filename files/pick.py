import Emp,pickle

f=open("emp1.dat",'wb')
n=int(input("How many employees:"))

for i in range(n):
    id=int(input("Enter ID:"))
    name=input("Enter the name:")
    sal=float(input("Enter sal:"))

    e= Emp.Emp(id,name,sal)

    pickle.dump(e,f)
f.close()
