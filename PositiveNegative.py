#Python program to print all positive and negative numbers in a specified range

#Sample Input
'''start = -10,end = 10'''
#Sample Output
'''
Negative numbers are : [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
Positive numbers are : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
start = -10
end = 10
lst1 = []
lst2= []
for i in range(start,end+1):
    if i < 0 :
        lst1.append(i)
    else:
        lst2.append(i)
print("Negative numbers are :",lst1)
print("Positive numbers are :",lst2)