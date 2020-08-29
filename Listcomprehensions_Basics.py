#Exercises on List Comprehension methods

#program1

str1 = "Python"
x = [print(i) for i in str1 if i not in "brinda"]

#Explanation
for i in str1:
    if i not in "brinda":
        print(i)

#Output 
'''
P
y
t
h
o
'''
#program2
str1 = "Python"
x = [print(i) for i in str1 if i not in "brinda"]
print(x)

#Explanation
for i in str1:
    if i not in "brinda":
        print(i)
print(x)

#Output
'''
P
y
t
h
o
[None, None, None, None, None]'''

#program3
str1 = "Python"
x = [(i.upper(), len(i)) for i in str1]
print(x)

#Explanation
str1 = "Python"
lst1 =[]
for i in str1:
    x = i.upper()
    y = len(i)
    lst = (x,y)
    lst1.append(lst)
print(lst1)
    
#Output([('P', 1), ('Y', 1), ('T', 1), ('H', 1), ('O', 1), ('N', 1)])

#program4
print([i+j for i in "abc" for j in "def"])

#Explanation
lst = []
for i in "abc":
    for j in "def":
        lst.append(i+j)
print(lst)

#Output(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])

#program5
print([[i+j for i in "abc"] for j in "def"])

#Explanation
lst1 = []
for j in "def":
    lst = []
    for i in "abc":
        lst.append(i + j)
    lst1.append(lst)
print(lst1)
        
#Output([['ad', 'bd', 'cd'], ['ae', 'be', 'ce'], ['af', 'bf', 'cf']])
