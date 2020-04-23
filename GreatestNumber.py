#Python program to find greatest number in a list

#Sample Input
'''list1 = [12,1,3,4,5,5,12,13,12,12,12,1,2,0,-1]'''
#Sample Output
'''Greatest number is : 13'''

list1 = [12,1,3,4,5,5,12,13,12,12,12,1,2,0,-1]
lar = list1[0]
for i in list1:
    if(lar < i):
        lar = i
print("Greatest number is :",lar)