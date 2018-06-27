from functools import *
 
lst=[5,6,7,8,9]

res=reduce(lambda x,y:x*y,lst)
print(res)