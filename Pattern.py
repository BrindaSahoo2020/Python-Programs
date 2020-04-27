#Python program to print a pattern 

#Sample Output
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

for i in range(6):
	for j in range (1,i+1):
		print('*',end=' ')
	print()