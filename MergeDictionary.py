#Python program tp merge two Dictionaries

#Sample Input
'''
dict1 = {'a': 2, 'b': 3} 
dict2 = {'c': 4, 'd': 5,'e':6} 
'''
#Sample Output
'''Merged dictionary : {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6}'''

dict1 = {'a': 2, 'b': 3} 
dict2 = {'c': 4, 'd': 5,'e':6} 
(dict1.update(dict2))
print("Merged dictionary :",dict1)
