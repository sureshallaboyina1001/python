#Sets DEMO

lst = [10,20,30,40,'suresh',40,30]
s=set(lst)
for i in s:
    print(i)
print("Sets Was Updated")

s.update([50,"sam"])

print(s)

print("Sets element was removed")
s.remove(30)
print(s)


# FrozenSet Demo

lst =[10,20,30,40,45,10]
fs = frozenset(lst)
for x in fs:
    print(x)
