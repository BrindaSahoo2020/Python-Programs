#Python program to check whether a number is Prime or not

#Sample Input
''' num = 8 ,num = 31 '''
#Sample Output
'''8 is not a prime number
31 is a prime number '''

num = int(input("Enter a number: "))  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           break  
   else:  
       print(num,"is a prime number")         
else:  
   print(num,"is not a prime number") 