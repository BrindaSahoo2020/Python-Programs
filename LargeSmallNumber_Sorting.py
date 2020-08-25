#Find the large number fromlist by using sort() method

L1 = [200,1,0,45,34,90,100,3000]
L1.sort(reverse = True)
print("The largest number is ",L1[0])
L1.sort()
print("The smallest number is ",L1[0])

#Output
'''
The largest number is  3000
The smallest number is  0
'''