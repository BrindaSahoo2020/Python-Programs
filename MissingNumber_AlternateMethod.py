#Find the missing number form the list
#Program1
arr1 = [1,2,4,5,7,8,23]
arr2 = [2,4,15]
arr3 = []
for i in arr1:
	if i not in arr2:
		arr3.append(i)
print("Missing numbers are : ",arr3)

#Output(Missing numbers are :  [1, 5, 7, 8, 23])

#Program2
arr1 = [101, 102, 104,109] 
arr2 = []
for i in range(101,109):
	if i not in arr1:
		arr2.append(i)
print("Missing numbers are ",arr2)

#Output(Missing numbers are  [103, 105, 106, 107, 108])