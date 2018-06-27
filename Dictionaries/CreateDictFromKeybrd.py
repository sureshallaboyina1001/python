#createa dictionary from Keyboard and Display

dict={}

print("How many elements:",end="")
n=int(input())

for i in range(n):
    print("Key :",end='')
    k=input()
    print("Value:",end='')
    v=int(input())
    dict.update({k:v})

print("The Dictionary:",dict)
