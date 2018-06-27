from array import *

arr = array("i",[10,20,30,40,50])
print("The elements in the array are", arr)


arr.append(30)
arr.append(70)

print("Array after appending the elements",arr)

arr.remove(40)
print("Array after removig the element:",arr)

arr.insert(5,7)
print("Array after inserting the element:",arr)

n=arr.index(50)
print("Array after indexing :",n)
 
arr1 = array("i",[10,20,30,40,40,50])
arr2=arr.extend(arr1)
print("Array after extending the element:",arr2)

print(arr1.count(40))
lst = arr.tolist()
print(lst)

