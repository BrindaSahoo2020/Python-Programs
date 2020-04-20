#Python program to print all Prime numbers between 1 to 50

#Sample Output
'''
Prime numbers between 1 to 50 are :
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''

lst=[]
for num in range(1,51):
	if num > 1:
		for i in range(2,num):
			if(num%i)==0:
				break
		else:
			lst.append(num)
print("Prime numbers between 1 to 50 are :")
print(lst)
	

