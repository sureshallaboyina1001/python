import Emp,pickle


f=open("emp1.dat",'rb')
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("End of file reached")
        break
f.close()
