#Find a number is armstrong or not

#Enter your own input nad check

num = int(input("Enter a number : "))
str1 = str(num)
sum1 = 0
l = len(str1)
for i in str1:
	i = int(i)**l
	sum1 = sum1+i
if (num == sum1):
	print(num," is armstrong number")
else:
	print(num," is not armstrong number")
