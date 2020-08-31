#Python program to check if a string is palindrome or not

#Enter your own input and verify

str1 = str(input("Enter a string : "))
str2 =""
for i in str1:
    str2 = i + str2
print("Reversed string is ",str2)
if (str1 == str2):
    print("String is palindrome")
else:
    print("String is not palindrome")