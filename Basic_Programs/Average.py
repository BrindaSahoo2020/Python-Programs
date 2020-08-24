#Calculate the average of  numbers in a list

lst = []
for i in range(1,20,5):
    lst.append(i)
print(lst)
l = len(lst)
total = 0
for i in lst:
    total = total+i
print(total)
avg = float(total/l)
print("Average of the list is ",avg)

#Output (Average of the list is  8.5)