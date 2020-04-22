#Python program to reverse an ip

#Sample Input
'''12.23.45.6'''
#Sample Output
'''6.45.23.12'''

ip = str(input("Enter an ip:"))
x = ip.split('.')
print('.'.join(x[::-1]))
