#Python Program to find n-th Fibonacci Series

#Sample Input
'''n = 10'''
#Sample Output
'''Fibonacci sequences are : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] '''
lst = []
n = int(input("Enter a number: "))  
n1 = 0
n2 = 1
count = 0
while count < n:
       lst.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
print("Fibonacci sequences are :",lst)