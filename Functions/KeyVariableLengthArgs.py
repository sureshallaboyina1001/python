def KeyVar(fargs,**kwargs):
    print("Formal Arguments:",fargs)

    for x,y in kwargs.items():
        print("key={},value={}".format(x,y))
KeyVar(5,rno=10)
KeyVar(10,name="suresh",roll_no=401)

