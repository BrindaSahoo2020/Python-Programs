#Python program to count the number of digits in a number

#Sample Input
#Enter number:1678950
#Sample Output
#he number of digits in the number are: 7

n = int(input("Enter number:"))
count = 0
while(n > 0):
    count = count+1
    n = n//10
print("The number of digits in the number are:",count)