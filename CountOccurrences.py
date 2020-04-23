#Python program to count occurrences of an element in a list

#Sample Input
''' list1 = [1,2,3,3,1,10,3,9]'''
#Sample Output
'''3 has occured 3 times'''

list1 = [1,2,3,3,1,10,3,9]
count = 0
n = int(input("Enter a number from list1:"))
for i in list1:
    if (i == 3):
        count+=1
print(n,"has occured",count,"times")


