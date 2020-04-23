#Python program to print N largest elements from a list

#Sample Input
'''[2080,67,34,90,20,0,9001,8000,100,1000,9,1,9004,600]'''
#Sample Output
'''4 largest numbers are : [9004, 9001, 8000, 2080]'''

L1 = [2080,67,34,90,20,0,9001,8000,100,1000,9,1,9004,600]
N = 4
L2 = []
for i in range(0,N):
	max1 = 0
	for j in range(len(L1)):
		if L1[j] > max1:
			max1 = L1[j]
	L1.remove(max1)
	L2.append(max1)
print (N,"largest numbers are :",L2)