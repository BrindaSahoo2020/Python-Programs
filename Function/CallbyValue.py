#Write a Python Program to describe Call By Value in function

str1 = "Brinda Sahoo"
def name(str1):
	print("Name :",str1)
#Driver's Code
name("Chanda Sahoo")
name(str1)
name("Aashna Samal")

#Output
'''('Name :', 'Chanda Sahoo')
('Name :', 'Brinda Sahoo')
('Name :', 'Aashna Samal')'''
