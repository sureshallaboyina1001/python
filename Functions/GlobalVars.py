a=1
def var():
    global a
    print("global=",a)
    a=2
    print("modified=",a)
var()
print("global=",a)