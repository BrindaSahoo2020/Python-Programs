#Python program to find the occurrence of each element in list 

#Sample Input
'''list1=[1,2,3,5,8,1,5]'''
#Sample Output
''' Frequency of occurrence of elements : {1: 2, 2: 1, 3: 1, 5: 2, 8: 1}'''

list1=[1,2,3,5,8,1,5]
freq ={}
for elem in list1:
	if elem in freq:
		freq[elem]=freq[elem]+1
	else:
		freq[elem]=1
print ("Frequency of occurrence of elements :",freq)
