#Python Program to check Armstrong Number

#Sample Input
n = 8208,67
#Sample Output
'''
8208 is an Armstrong number
67 is not an Armstrong number
'''

num = int(input("Enter a number: "))
'''Changed num variable to string, to calculate the length (number of digits)'''
l = len(str(num))
sum1 = 0
'''find the sum of the power of each digit'''
temp = num
while temp > 0:
   digit = temp % 10
   sum1 = sum1+ digit ** l
   temp = temp//10
'''display the result'''
if num == sum1:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
