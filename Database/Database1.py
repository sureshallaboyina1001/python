import mysql.connector

conn=mysql.connector.connect(host="localhost",database='employee',user='root',password="Suresh1$")
cursor=conn.cursor()
cursor.execute("select * from emp")
rows=cursor.fetchone()

while rows is not None:
    print(rows)
    rows=cursor.fetchone()
cursor.close()
conn.close()

