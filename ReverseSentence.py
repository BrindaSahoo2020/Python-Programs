#Python program to reverse a sentence

#Sample Input
'''I am new to python programming'''
#Sample Output
'''Reversed sentence is : programming python to new am I'''

str1 = str(input("Enter a sentence:"))
word = str1.split()
output = word[-1::-1]
str2 = " ".join(output)
print ("Reversed sentence is :",str2)
