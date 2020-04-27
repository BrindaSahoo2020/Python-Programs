#Python program to remove duplicates and reprint the list 

#Sample Input
'''test_list = [1,3,5,6,3,4,4,2,2,5,6,1]'''
#Sample Output
'''Final list is : [1, 3, 5, 6, 4, 2]'''

test_list = [1,3,5,6,3,4,4,2,2,5,6,1]
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i) 
print ("Final list is :",res)
