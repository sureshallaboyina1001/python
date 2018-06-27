str="10=suresh,20=sam,30=ramesh,40=suma"
lst=[]

for x in str.split(','):
    print(x)
    y=x.split('=')
    lst.append(y)

print("List:",lst)

d=dict(lst)
print(d)
