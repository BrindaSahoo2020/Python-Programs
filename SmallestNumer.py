#Python program to find smallest number in a list

#Sample Input
'''list1 = [12,1,3,4,5,5,12,13,12,12,12,1,2,0,-1]'''
#Sample Output
'''Smallest number is -1'''

list1 = [12,1,3,4,5,5,12,13,12,12,12,1,2,0,-1]
sma = list1[0]
for i in list1:
    if (sma > i):
        sma = i
print("Smallest number is :",sma)