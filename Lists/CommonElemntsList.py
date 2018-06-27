#Retreive Common element in list

lst1=["suresh","priya","prgana","sushmita","suma"]
lst2=["suresh","priya","prgana","samantha","shruthi"]

s1=set(lst1)
print(s1)
s2=set(lst2)
print(s2)

s3=s1.intersection(s2)
print(s3)

lst3=list(s3)
lst3.sort(reverse=True)
print("list :",lst3)
