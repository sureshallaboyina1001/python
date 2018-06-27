import mysql.connector

def insert(eno,ename,sal):
    conn=mysql.connector.connect(host="localhost",database="employee",user="root",password="Suresh1$")
    if conn.is_connected():
        print("Connected to the database")
    cursor=conn.cursor()
    str="insert into emp(eno,ename,sal) values('%d','%s','%f')"
    args=(eno,ename,sal)
    try:
        cursor.execute(str % args)
        conn.commit()
        print("1 row inserted")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

n=int(input("How many records to insert:"))
for i in range(n):
    x=int(input("Enter employee no:"))
    y=input("Enter the employee name:")
    z=float(input("Enter the employee salary:"))
    insert(x,y,z)
    print("-----------------------")
       