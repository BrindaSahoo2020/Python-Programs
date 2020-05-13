#Simple python program on selection sort
#It works by repeatedly finding the minimum element from unsorted part and putting it at the beginning.

#Sample Output
#Sorted elements are : [11, 12, 22, 25, 64, 101, 300]

L1 = [64,25,12,22,11,101,300] 
l = len(L1)
for i in range(l):
	# Find the minimum element in remaining unsorted array 
	min_elem = i
	for j in range(i+1,l): 
		if L1[min_elem] > L1[j]: 
            		min_elem = j 
	L1[i],L1[min_elem] = L1[min_elem],L1[i] 
lst =[]
for i in range(l): 
    lst.append(L1[i])	
print ("Sorted elements are :",lst) 