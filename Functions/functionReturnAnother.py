def fun1():
    def message():
        return "HELLO Suresh"
    return message
fun=fun1()
print(fun())
