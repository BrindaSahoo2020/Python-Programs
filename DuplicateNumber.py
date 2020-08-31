#Python program to print the duplicates from a list of integers

#Sample Input
'''L1 = [10,10,75, 21,-1,-4,-5,-1,-5,4,45, 4]'''
#Sample Output
'''List of duplicates are : [10, -1, -5, 4]'''

L1 = [10,10,75, 21,-1,-4,-5,-1,-5,4,45, 4]
l = len(L1)
L2 = []
for i in range(l) :
    for j in range(i+1,l):
        if L1[i] == L1[j] and L1[i] not in L2:
            L2.append(L1[i])
print("List of duplicates are :",L2)

#Alternate method

L1 = [10,10,75, 21,-1,-4,-5,-1,-5,4,45, 4]
L2 = []
L3 =[]
for i in L1:
	if i not in L2:
		L2.append(i)	
	else:
		L3.append(i)
print("After removing duplicates :",L2)
print("List of duplicates are :",L3)


