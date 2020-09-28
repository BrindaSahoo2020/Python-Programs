#Program to find the sum of all items in a dictionary

d = {'a':100,'b':200,'c':300,'d':400,'e':500}
sum1 = 0
for i in d:
    sum1 = sum1 + d[i]
print("Sum is : ",sum1)

#Alternate Method
d = {'a':100,'b':200,'c':300,'d':400,'e':500}
sum1 = 0
for i in d.values(): 
    sum1 = sum1 + i 
print("Sum is : ",sum1)

#Output (Sum is :  1500)

#To remove a key from dictionary

d = {'a':100,'b':200,'c':300,'d':400,'e':500}
del d['a']
print(d)

#Output({'b': 200, 'c': 300, 'd': 400, 'e': 500})

#Merging two Dictionaries

d1 = {'a':100,'b':200,'c':300}
d2 = {'d':400,'e':500,'f':600}
d1.update(d2)
print(d1)

#Output ({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500, 'f': 600})

