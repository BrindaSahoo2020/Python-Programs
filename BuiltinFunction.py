#Important builtin functions
#pop()
L1 = [1,2,3,4,5,6,7,8]
L1.pop()
print(L1)
L1.pop(3)
print(L1)
#Output
'''
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 5, 6, 7]
'''

#zip()
name = [ "Aashna", "Srijitsi", "Nafya", "Ayushi" ] 
roll_no = [ 1, 28, 3, 2 ] 
marks = [ 45, 42, 40, 40 ] 
mapped = zip(name, roll_no, marks)
# converting values to print as set 
mapped = set(mapped) 
print(mapped)
#Output
'''
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 5, 6, 7]
{('Ayushi', 2, 40), ('Nafya', 3, 40), ('Aashna', 1, 45), ('Srijitsi', 28, 42)}
'''

#insert()
L1 = [1,2,3,4,5]
L1.insert(2,8)
print(L1)
#Output
#[1, 2, 8, 3, 4, 5]

#extend()
L1 = [1,2,3,4,5]
L2= [9,0]
L1.extend(L2)
print(L1)
#Output
#[1, 2, 3, 4, 5, 9, 0]

#append()
animal = ['cat', 'dog', 'rabbit']
animal.append(['guinea pig'])
print('Updated animal list: ', animal)
#Output
# Updated animal list:  ['cat', 'dog', 'rabbit', ['guinea pig']]

#index()
L1 = [2,3,4,5,6]
print("Index of 6 is :" ,L1.index(6))
#Output
#Index of 6 is : 4

#sort()
vowels=['u','e','o','a','i']
vowels.sort()
print(vowels)
#Output
#['a', 'e', 'i', 'o', 'u']

#count()
list1 = [8,9,0,7,7,7,7]
print("Count of 7 is :",list1.count(7))
#Output
#Count of 7 is : 4

#reverse()
list1 = [8,9,0,7,7,7,7]
list1.reverse()
print(list1)
#Output
#[7, 7, 7, 7, 0, 9, 8]

#copy()
list1 = [2,3,4,5,6]
list2 = list1.copy()
print(list2)
#Output
#[2, 3, 4, 5, 6]

#clear()
list1 = [2,3,4,5,6]
list1.clear()
print(list1)
#Output
#[]