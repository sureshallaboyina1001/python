dict={'r':"red",'b':"BLUE",'g':"Green",'o':"Orange"}

d1=sorted(dict.items(),key=lambda t:t[0])
print(d1)

dict={'id':1001,'name':"BLUE",'Salary':50000}
d2=sorted(dict.items(),key=lambda x:x[0])
print(d2)
