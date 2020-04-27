#Python program to remove any character from string

#Sample Input
'''Learn Python'''
#Sample OutPut
'''New string is : Lean Python'''

str1="Learn Python"
#Removing 3rd index
if str1[3] == 'r':
	str2 = str1.replace('r',"")
print("New string is :",str2)
