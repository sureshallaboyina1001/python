import cx_Oracle

conn = cx_Oracle.connect('scott/tiger@localhost')
cursor = conn.cursor()
cursor.execute("select * from emp")
row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()
