#Python program to find power of each element in the list

#Sample Input
'''lst1 = [1,2,3,4,5,6,7,8,9,10]'''
#Sample Output
'''Result : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]'''

lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = []
for elem in lst1:
    pow = elem **2
    lst2.append(pow)
print("Result :",lst2)