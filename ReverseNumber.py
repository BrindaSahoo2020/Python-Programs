#Python program to Reverse a Given Number

#Sample Input
'''1278'''
#Sample Output
'''Reverse of the number: 8721'''

n = int(input("Enter number: "))
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
print("Reverse of the number:",rev)
