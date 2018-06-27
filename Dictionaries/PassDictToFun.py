#Passing Dictionary to Function

def dictfun(dict):
    for k,v in dict.items():
        print(k,":",v)

d=eval(input("Enter the elements{}:"))
dictfun(d)
