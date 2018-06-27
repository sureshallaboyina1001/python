from collections import OrderedDict

d=OrderedDict()
d[10]='A'
d[12]='C'
d[11]='B'
d[9]='D'

for k,v in d.items():
    print(k,v)
