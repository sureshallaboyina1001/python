#List Comprehension

squares=[x*x for x in range(1,11)]
print(squares)


#Add two list with each element
x=[2,3,4,5,8]
y=[3,4,5,6,2]
print(x)
print(y)
lst=[i+j for i in x for j in y]
print(lst)


dict={1001:"suresh",1002:"Anand",1003:"Yellaji"}
dict1={value:key for key,value in dict.items()}
print(dict1)
