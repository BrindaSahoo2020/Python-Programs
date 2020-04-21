#Python program to find length of a list without built-in function

#Sample Input
'''lst = [1,3,5,78,90,89,45,67,0,2,4,50]'''
#Sample Output
'''Length of the list is: 12'''

lst = [1,3,5,78,90,89,45,67,0,2,4,50]
l = 0
for i in lst:
    l+=1
print("Length of the list is:",l)