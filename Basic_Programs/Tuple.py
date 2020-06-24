#Python program to create a list of tuples from a list having number & its cube in each tuple

#Sample Input
list1 = [2,3,4,5]
#Sample Output
#Result is : [(2,8), (3, 27), (4, 64),(5,125)]

list1 = [2,3,4,5]
#printing result using list comprehension
res = [(i, pow(i, 3)) for i in list1] 
print ("Result is :",res)