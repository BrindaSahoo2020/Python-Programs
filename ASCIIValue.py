#Python program to print ASCII Value of a character and string

#Sample Input
''' Enter any character :c '''
#Sample Output
'''
ASCII value is  99
ASCII values of the strings are : [98, 114, 105, 110, 100, 97]
'''

ch = str(input("Enter any character :"))
x = ord(ch)
print("ASCII value is " ,x)
str1 = "brinda"
lst1 = []
for i in str1:
	lst1.append(ord(i))
print("ASCII values of the strings are :", lst1)