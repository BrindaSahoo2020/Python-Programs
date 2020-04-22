#Python program to reserve a string

#Sample Input
''' Brinda Sahoo '''
#Sample Output
''' Reversed string is : oohaS adnirB'''

str1 = str(input("Enter the string :"))
str2 = ""
for i in str1:
    str2 = i + str2
print("Reversed string is :",str2)