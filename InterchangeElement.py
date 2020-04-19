#Python program to interchange first and last elements in a list

#Sample Input
'''L1 = [12,100,15,56,78,90,67]'''
#Sample Output
'''
The list after interchange of first and last element is : [67, 100, 15, 56, 78, 90, 12]
'''

L1 = [12,100,15,56,78,90,67]
l = len(L1)
temp = L1[0]
L1[0] = L1[l-1]
L1[l-1] = temp
print("The list after interchange of first and last element is :",L1)