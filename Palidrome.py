#Python program to check a number is palidrome is not.

#Sample Input
'''12221,34598'''
#Sample Output
'''
12221 is palindrome!
34598 isn't palindrome!
'''

n = int(input("Enter a number: "))
rev = 0
temp = n
while n > 0:
    a = n % 10 
    rev = rev * 10 + a
    n = n // 10
if(temp == rev):
    print(temp,"is palindrome!")
else:
    print(temp,"isn't palindrome!")