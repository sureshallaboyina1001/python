# using loops
dict={'r':"red",'b':"BLUE",'g':"Green",'o':"Orange"}
for k in dict:
    print(k)

for k in dict:
    print(dict[k])

for k,v in dict.items():
    print("Key={} ,Value={}".format(k,v))
