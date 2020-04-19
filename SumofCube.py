#Python Program for Sum of squares of first n natural numbers

#Sample Input
'''
n = 10
'''
#Sample Output
'''Result is :  385'''

n = int(input("Enter a number : "))
sum1 = 0
for i in range(1,n+1):
    sum1 = sum1 + (i*i)
print("Result is : ",sum1)

