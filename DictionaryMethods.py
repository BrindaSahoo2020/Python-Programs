#Python programs on different Dictionary Methods

#Adding Items
dict1 =	{"School":"NHPS","Year":2020,"Class":4,"Name":"Aashna","RollNo":2}
dict1["Subject"] = "Math"
print(dict1)
#Output
'''
{'School': 'NHPS', 'Year': 2020, 'Class': 4, 'Name': 'Aashna', 'RollNo': 2, 'Subject': 'Math'}
'''
#Removing Items - Method1
dict1 =	{"School":"NHPS","Year":2020,"Class":4,"Name":"Aashna","RollNo":2}
dict1.pop("School")
print(dict1)
#Output
#{'Year': 2020, 'Class': 4, 'Name': 'Aashna', 'RollNo': 2}
#Removing Items - Method2
dict1 =	{"School":"NHPS","Year":2020,"Class":4,"Name":"Aashna","RollNo":2}
del dict1["School"]
print(dict1)
#Output
#{'Year': 2020, 'Class': 4, 'Name': 'Aashna', 'RollNo': 2}

#Clear the Dictionary
dict1 =	{"School":"NHPS","Year":2020,"Class":4,"Name":"Aashna","RollNo":2}
dict1.clear()
print(dict1)
#Output
#{}
#Copy a Dictionary
dict1 =	{"School":"NHPS","Year":2020,"Class":4,"Name":"Aashna","RollNo":2}
dict2 = dict1.copy()
print(dict2)
#Output
#{'School': 'NHPS', 'Year': 2020, 'Class': 4, 'Name': 'Aashna', 'RollNo': 2}
#Other Methods
'''
get()	Returns the value of the specified key
keys()	Returns a list containing the dictionary's keys
popitem()	Removes the last inserted key-value pair
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''