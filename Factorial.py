#Python Program to find factorial of a number

#Sample Input
'''n = 8'''
#Samsple Output
'''Factorial of 8 is 40320'''

n = int(input("Enter the number : "))
fact = 1
if (n==0):
	print("Factorial of {0} is {1}".format(n , fact))
elif (n < 0):
	print("Fatorial of negative number is not possible")
else:
	for i in range(1,n+1):
		fact = fact*i
	print("Factorial of {0} is {1}".format(n , fact))
