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

for pnames in dict.keys():
    print(pnames)
print("enter the player name:",end="")
name=input()

runs=dict.get(name,-1)

if(runs == -1):
    print("Player not found:")
else:
    print("{} scores {}".format(name,runs))

