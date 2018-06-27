#Add all the elements in the list using for loop

list = [10,20,30,40,50]
sum=0
for ctr in list:
    sum+=ctr
print("Using For Loop")
print("sum is",sum)

i=0
while i<len(list):
    sum+=list[i]
    i+=1
print("Using while Loop")
print("sum is",sum)
     


