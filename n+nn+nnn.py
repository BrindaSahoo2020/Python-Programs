#Python Program to read a number n and compute n+nn+nnn

#Sample Input
'''
Enter n value :4
Enter m value:4
'''
#Sample Output
#Result is : 4936

n = int(input("Enter n value :"))
m = int(input("Enter m value:" ))
str_n = str(n) 
sums = n 
sum_str = str(n) 
for i in range(1, m): 
    sum_str = sum_str + str_n 
    sums = sums + int(sum_str)
print ("Result is :",sums)