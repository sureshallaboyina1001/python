f=lambda x:x*x
value=f(5)
print("Square value =",value)

x = lambda a,b:a+b
res=x(5,6)
print("sum is %d" % res)

func=lambda x:'yes' if x%2==0 else 'no'
res = func(34)
print(res)