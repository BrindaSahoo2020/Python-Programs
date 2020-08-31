#Python program to count the number of digits in a number

#Sample Input
#Enter number:1678950
#Sample Output
#The number of digits in the number are: 7

n = int(input("Enter number:"))
count = 0
while(n > 0):
    count = count+1
    n = n//10
print("The number of digits in the number are:",count)

#Method2

n = int(input("Enter number:"))
n1 = str(n)
count = 0
l = len(n1)
for i in range(l):
	count = count + 1
print("The number of digits in the number are:",count)
	