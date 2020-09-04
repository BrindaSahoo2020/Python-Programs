#Python program on linear search

#Sample Input
#6,100
#SampleOutput
#Element is found at index : 4
#Element is not found

L1 = [1,3,5,4,6,0,90,89]
x = int(input("Enter a number : "))
l = len(L1)
for i in range (l):
	if L1[i] == x :
		print("Element is found at index :",i)
		break
else:
	print("Element is not found")

