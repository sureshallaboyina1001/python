#First Occurence  of element in list

str=input("Enter the elements:").split(',')

lst=[int(num)for num in str]

tpl=tuple(lst)

print("The tuple:",tpl)

ele=int(input("enter the elements:"))

try:
    pos=tpl.index(ele)
    print("Element Position no:",pos)
except ValueError:
    print("Element not found")
    
