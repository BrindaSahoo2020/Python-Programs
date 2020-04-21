#Python program to print all the numbers between 0 to 100 skipping 10 

#Sample Output
'''List after skipping 10 is : [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

lst = []
for i in range(0,101,10):
    lst.append(i)
print("List after skipping 10 is :",lst)