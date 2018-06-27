#To print Armstrong number 
 
min = int(input('Enter a min number: '))
max = int(input('Enter a max number: '))

for num in range(min,max+1):  
    sum = 0  
     
    temp = num	
    while temp > 0:  
        rem = temp % 10  
        sum += rem ** 3  
        temp //= 10 
       
        if (num==sum):
            print(num)  

  