#Print all Keys and Values in the dictionary, one by one

#Sample OutPut
'''
Keys are : ['school', 'year', 'class', 'Name', 'RollNo']
Values are : ['NHPS', 2020, 4, 'Aashna', 2]
'''

dict1 =	{"school":"NHPS","year":2020,"class":4,"Name":"Aashna","RollNo":2}
lst1 = []
lst2 = []
for x in dict1:
    lst2.append(x)
print("Keys are :",lst2)
for x in dict1:
    lst1.append(dict1[x])
print("Values are :",lst1)