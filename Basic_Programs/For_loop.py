#Simple python programs on FOR LOOP
#Program1

dict1 = {0: 'a', 1: 'b', 2: 'c'}
for x, y in dict1.items():
    print(x, y)

#Output :
'''
0 a
1 b    
2 c
'''
#Program2

dict1 = {0: 'a', 1: 'b', 2: 'c'}
for x in dict1.keys():
    print(dict1[x])

#Output :a b c

#Program3

dict1 = {0: 'a', 1: 'b', 2: 'c'}
for x in dict1.values():
    print(x)

#Output :a b c

#Program4

x = 2
for i in range(x):
    x += 1
    print (x)

#Output : 3 4