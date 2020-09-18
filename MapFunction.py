#The map() function executes a specified function for each item in an iterable.
#Syntax : map(function,iterables)

def uppercase(x):
    return x.upper()
y = ['ab', 'cd']
print(list(map(uppercase, y)))

#Output (['AB', 'CD'])

x = ['ab', 'cd']
print(list(map(len, x)))

#Output ([2, 2]) #Length of each string is 2

x = ['ab', 'cd']
print(list(map(list, x)))
print(len(list(map(list, x))))

#Output 
'''
[['a', 'b'], ['c', 'd']]
2
'''

lst = [1,2,3]
def increment(x):
    return x+1
print(list(map(increment, lst)))

#Output ([2, 3, 4])
'''
x = [12, 34]
print(len(list(map(len, x))))
'''
#output(TypeError: object of type 'int' has no len())

x = [24, 37]
print(len(list(map(int, x))))

#Output (2)

x = [24, 367]
print(''.join(list(map(str, x))))
print(len(''.join(list(map(str, x)))))

#Output 
'''
24367
5
'''

