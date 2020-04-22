#Python program for Reversing a List without slice operation and built-in function

#Sample Input
'''L1 = [1,2,3,4,5,6,7,8,9,0]'''
#Sample Output
'''Reversed list is : [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]'''

L1 = [1,2,3,4,5,6,7,8,9,0]
l = len(L1)
i = l+1
L2 = []
while l > 0 :
    j = i - l
    l = l - 1
    L2.append(L1[-j])
print("Reversed list is :",L2)