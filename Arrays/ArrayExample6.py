#storing Students marks into an array.
#calculate total and percenatge of the marks.

from array import *

str = input("Enter marks:").split(' ')

marks = [int(num)for num in str]

sum=0
for i in marks:
    print(i)
    sum+=i
print("total Marks :",sum)

n= len(marks)
percent =sum/n
print("percentage:", percent)