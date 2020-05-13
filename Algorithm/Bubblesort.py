#Simple python program on bubble sort
#It works by repeatedly swapping the adjacent elements if they are in wrong order.

#Sample Output
#Sorted list is : [90, 89, 6, 5, 4, 3, 1, 0]

L1 = [1,3,5,4,6,0,90,89]
l = len(L1)
for i in range(l):
	for j in range(l-1):
		if (L1[j]< L1[j+1]):
			L1[j],L1[j+1] = L1[j+1],L1[j]
print("Sorted list is :",L1)