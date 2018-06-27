str="viajy=23,suresh=25,lakshmi=18,nikhil=22"
lst=[]
for x in str.split(','):
    print(x)
    y=x.split('=')
    print(y)
    lst.append(y)
print(lst)
d=dict(lst)
print(d)
