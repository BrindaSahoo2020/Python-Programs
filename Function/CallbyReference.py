#Write a Python Program to describe Call By Reference in function

def sum(lst): 
    lst.append(6) 
    print("Final list:", lst) 
  
# Driver's code 
lst1 = [1,2,3,4,5] 
  
sum(lst1) 
print("Final list:", lst1) 

#output
'''
('Final list:', [1, 2, 3, 4, 5, 6])
('Final list:', [1, 2, 3, 4, 5, 6])
'''