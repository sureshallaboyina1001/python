def fun1(str):
    def fun2():
        return "Hello!How are you?"
    result=fun2()+ str
    return result
res = fun1("Suresh")
print(res)
