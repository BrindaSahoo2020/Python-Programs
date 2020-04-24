#Python program to print even and odd numbers in a list

#Sample Input
'''L1 = [20080,67,34,90,20,0,100,1000,9,1,9004,3,5,7,10,20,33,31,32]'''
#Sample Output
'''
Even numbers are : [20080, 34, 90, 20, 0, 100, 1000, 9004, 10, 20, 32]
Odd numbers are : [67, 9, 1, 3, 5, 7, 33, 31]
'''

L1 = [20080,67,34,90,20,0,100,1000,9,1,9004,3,5,7,10,20,33,31,32]
L2 = []
L3 = []
for num in L1:
    if (num%2 == 0):
        L2.append(num)
    else:
        L3.append(num)
print("Even numbers are :",L2)
print ("Odd numbers are :",L3)
