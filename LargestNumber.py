#Python program to find the largest number in a list

#Sample Input
'''list1 = [12,14,3,4,5,5,12,13,12,120,12,100,2,0,-1]'''
#Sample Output
'''Largest number is 120'''

list1 = [12,14,3,4,5,5,12,13,12,120,12,100,2,0,-1]
l =len(list1)
lar = list1[0]
for i in range(l):
    if (lar < list1[i]):
        lar = list1[i]
print ("Largest number is ", lar)
