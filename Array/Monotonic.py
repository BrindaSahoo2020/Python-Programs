#Python Program to check if given array is Monotonic

#Arr = [1,1,2,2,3,4,5]
#Arr = [40,30,30,20,10,10,0]
Arr = [40,50,30,20,10,10,0]
l = len(Arr)
if (all(Arr[i] <= Arr[i + 1] for i in range(l - 1)) or all(Arr[i] >= Arr[i + 1] for i in range(l - 1))) :
    print("Array is monotonic")
else:
    print("Array is not monotonic")

#Verify your own ans