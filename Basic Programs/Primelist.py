#to print prime number list

min=int(input('enter a min number: '))
max=int(input('enter max number: '))

for num in range(min,max):  
   if num >1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 