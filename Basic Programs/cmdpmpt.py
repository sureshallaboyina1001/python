#accept group of numbers from cmd and fine their sum and avg

from sys import *
lst=argv
n= len(lst)
print('no of elemnets=',n-1)
sum =0
for i in range(1,n):
    sum+=float(lst[i])
print('sum :',sum)
print('average :',sum/(n-1))
