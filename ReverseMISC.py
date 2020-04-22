#Reverse the string retaining the position of special character 

#Sample Input
'''abc@#$hjk78%^&*hj*'''
#Sample Output
'''jh8@#$7kjhc%^&*ba*'''

str1 = str(input("Enter the string : "))
list1 = list(str1)
l1 = len(list1)
l = 0
r = l1 - 1 

while l < r:
	if not list1[l].isalnum():
		l+=1
	elif not list1[r].isalnum():
		r-=1
	else:
		list1[l],list1[r] = list1[r] ,list1[l]
		l+=1
		r-=1
print("".join(list1))
