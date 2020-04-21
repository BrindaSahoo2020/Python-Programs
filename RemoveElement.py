#Python program to remove Nth element from the list

#Sample Input
'''list1 = [1,3,7,9,0,56]'''
#Sample Output
'''New list after removing the element :  [1, 3, 9, 0, 56] '''

list1 = [1,3,7,9,0,56]
list2 = []
pos = int(input("Index from list user want to remove :"))
l = len(list1)
for i in range(l):
    if (i != pos):
        list2.append(list1[i])
print("New list after removing the element : ",list2)
