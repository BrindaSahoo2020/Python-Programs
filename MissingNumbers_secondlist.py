#Find elements which are present in first array and not in second

#Sample Input (arr1 = [1,2,4,5,7,8,23] arr2 = [2,4,15])

#Sample Output : arr3 = [1, 5, 7, 8, 23]

arr1 = [1,2,4,5,7,8,23]
l1 = len(arr1)
arr2 = [2,4,15]
l2 = len(arr2)
arr3 = []
for i in range(l1):
    for j in range(l2):
        if (arr1[i] == arr2[j]):
            break
    else: 
        arr3.append(arr1[i])
print(arr3)
