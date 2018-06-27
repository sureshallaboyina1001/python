#Accepting and Entering employee details

employees=[]

print("How many employee :",end="")
n=int(input())

for i in range(n):
    print("Enter EmpID:",end="")
    employees.append(int(input()))
    print("Enter EmpName:",end="")
    employees.append(input())
    print("Enter EmpSalary:",end="")
    employees.append(float(input()))

print("The employee Deatils:",employees)

id= int(input("enter the employee id:"))


for i in range(len(employees)):
    if id==employees[i]:
        print("EmpID={}\nEname={}\nEmpSalary={:.2f}".format(employees[i],employees[i+1],employees[i+2]))
        break
              
    
