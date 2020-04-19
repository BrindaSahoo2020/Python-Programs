#Python program to get a list as input from user

#Sample Input
'''num = 8, elem = 12 1 4 0 7 9 11 3'''
#Sample Output
'''The list is : [12, 1, 4, 0, 7, 9, 11, 3]'''

lst = [] 
num = int(input("Enter number of elements : "))
for i in range(0,num):
    elem = int(input())
    lst.append(elem)
print("The list is :",lst)




