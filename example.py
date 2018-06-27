str1 = input("enter input1:").split(',')
lst1 = [int(num) for num in str1]
tup1 =tuple(lst1)
print(tup1)

str2 = input("enter input2:").split(',')
lst2 = [int(num) for num in str2]
tup2 =tuple(lst2)
print(tup2)
lst3 = [x for x in tup1 if x in tup2]
print(lst3)