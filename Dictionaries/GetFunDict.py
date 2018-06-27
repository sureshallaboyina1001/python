dict={}
str="Book provides wisdom"
for x in str:
    dict[x]=dict.get(x,0)+1

for k,v in dict.items():
    print("key={}\t  its occurrence={}".format(k,v))
