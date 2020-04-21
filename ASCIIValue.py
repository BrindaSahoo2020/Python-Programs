#Python program to print ASCII Value of a character

#Sample Input
''' c '''
#Sample Output
'''ASCII value is 99'''

str1 = str(input("Enter a character : "))
for i in str1:
    print("ASCII value is",ord(i))
