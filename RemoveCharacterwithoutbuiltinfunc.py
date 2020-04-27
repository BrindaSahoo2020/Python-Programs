#Python program to remove nth character from string without builtin function

#Sample Input
'''Learn Python'''
#Sample OutPut
'''New string is : Lean Python'''

str1 = "Learn Python"
str2 = ""
l = len(str1)
#Removing 3rd index
for i in range(0 ,l):
	if (i != 3):
		str2 = str2 + str1[i]
print("New string is :",str2)