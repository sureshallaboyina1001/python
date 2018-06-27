#2 D array

from numpy import *

arr = array([[1,2,3],[4,5,6],[9,8,7]])
for i in range(len(arr)):
    print(arr[i])

n = len(arr)


arr1 = array([
		[[1,2,3],[4,5,6]],
		[[2,5,8],[9,8,7]]
		])
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        for k in range(len(arr1[i][j])):
            print(arr1[i][j][k],end="\t")
        print()
    print()