def is_even(x):
    if x%2==0:
       return True
    else:
        return False
lst=[10,20,56,17,85,96]
lst1=list(filter(is_even,lst))
print(lst1)

lst=[10,20,56,17,85,96]
f= list(filter(lambda x:(x%2==0),lst))
print(f)