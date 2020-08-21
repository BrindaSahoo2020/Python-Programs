#Count pairs with given sum in python

#Sample Input
'''arr1 = [2,5,8,9,0,7,1]
sum1 = 9'''

#Sample Output 
'''count euals to 3'''

arr1 = [2,5,8,9,0,7,1]
sum1 = 9
l = len(arr1)
count = 0
for i in range(0,l):
    for j in range(i + 1, l): 
            if arr1[i] + arr1[j] == sum1: 
                count += 1
print("count euals to ",count)