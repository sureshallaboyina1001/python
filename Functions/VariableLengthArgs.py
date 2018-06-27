def add(fargs,*args):
    print("Formal Argument=",fargs)
    sum=0
    for i in args:
        sum+=i
    print("Sum of args=",(fargs+sum))
add(5,10)
add(5,10,25,25,30)
