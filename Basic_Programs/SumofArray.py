#Python Program to find sum of array

#Sample Input
#arr = [1,3,5,7,9]
#Sample Output
#Sum of an array is : 25

#Method1
arr = [1,3,5,7,9]
sum = 0
for i in arr:
    sum = sum + i
print("Sum of an array is :",sum)

#Method2
arr = [1,3,5,7,9]
sum = 0
l = len(arr)
for i in range(l):
    sum = sum + arr[i]
print("Sum of an array is :",sum)
