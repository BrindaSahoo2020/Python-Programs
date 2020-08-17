#Find the Missing Numbers from a list

#Sample Input : lst = [101, 102, 104,109,108] 

#Sample Output : Missing numbers are : [103, 105, 106, 107]

lst1 = []
lst = [101, 102, 104,109,108] 
for i in range(lst[0], lst[-1]+1):
    if i not in lst:
        lst1.append(i)
print("Missing numbers are :",lst1)