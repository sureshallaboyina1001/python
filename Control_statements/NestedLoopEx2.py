#Nested loop example

for i in range(1,11):
   print("* "*(i))


for x in range(1,11):
    for y in range(1,11):
        print('{:2d}'.format(x*y), end=" ")
    print()