def decfun(fun):
    def inner():
        value=fun()
        print(value)
        return value+2
    return inner

@decfun
def num():
    return 10

print(num())