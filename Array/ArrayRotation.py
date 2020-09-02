#Python program to left rotate the elements of an array

arr = [1,2,3,4,5,6,7,8]   
n = 3
l = len(arr)  
   
for i in range(0, n):    
    first = arr[0];       
    for j in range(0, l-1):    
        #Shift element of array by one    
        arr[j] = arr[j+1];           
    #First element of array will be added to the end    
    arr[l-1] = first; 
arr1 = []

for i in range(0, len(arr)):    
    arr1.append(arr[i])   
print(arr1)

#Output([4, 5, 6, 7, 8, 1, 2, 3])
