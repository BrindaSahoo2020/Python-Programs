#Python program to find the cubes of each element in list and print

#Sample Input
list1 = [1,2,3,4,5,6]

#Sample Output
#Result : [1, 8, 27, 64, 125, 216]

list1 = [1,2,3,4,5,6]
list2 = []
for i in list1:
    cube = i*i*i
    list2.append(cube)
print("Result :",list2)