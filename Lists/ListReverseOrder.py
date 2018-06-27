#to print the list in reverse order
lst=["sunday","monday","tuesday","wednesday","Thursday"]
i=len(lst)-1
while i>=0:
    print(lst[i])
    i-=1
print("reverse Order")

i=-1

while i>=-len(lst):
    print(lst[i])
    i-=1
