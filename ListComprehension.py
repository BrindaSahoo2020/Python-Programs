#Basics of List-comprehensions in python

#General Method
lst = [1,2,3,4,5,6,7,8]
lst1 = []
for i in lst:
    lst1.append(i)
print(lst1)

#List-Comprehension Method
lst2 = [1,2,3,4,5,6,7,8]
print ([i for i in lst2 ])

#Output
'''
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]
'''