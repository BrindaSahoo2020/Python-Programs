#Python program to find second largest number in a list

#Sample Input
'''L1 = [2080,67,34,90,20,0,9001,8000,100,1000,9,1,9004,600]'''
#Sample Output
''' Second largest number is : 9001'''

L1 = [2080,67,34,90,20,0,9001,8000,100,1000,9,1,9004,600]
max1 = 0
max2 = 0
for elem in L1:
    if (max1 < elem):
        max2 = max1
        max1 = elem
    elif(max2 < elem):
        max2 = elem
print("Second largest number is :",max2)

