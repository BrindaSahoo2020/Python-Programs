#Python program to remove multiple elements from a list using slice operation

#Sample Input
'''Remove 1st to 5th element'''
#Sample Output
'''After removal of elements from index 1 to 5 : [10, 23, 45, 67, 22, 20, 4, 45]'''

L1 = [10, 21,-1,-4,-5,-722,23,45,67,22,20, 4, 45]
del L1[1:6]
print("After removal of elements from index 1 to 5 :",L1)
