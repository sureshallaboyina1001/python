from sys import *
#to list the arguments
n = len(argv)
args=argv
print("the arguments are",args)
print("the no of arguments are",n)
for a in args:
    print(a)
# sum of number from command Prompt
args=argv[1:]
sum=0
print("the args are",args)
for a in args:
    x=int(a)
    sum+=x
print("Sum is :",sum)
