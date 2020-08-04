#Given an array containing None values, fill in the None values with most recent 

#Sample Input
#arr3 = [1,None,2,3,None,None,5,None,None,6]

#Sample Output
#[1, 1, 2, 3, 3, 3, 5, 5, 5, 6]

def mysolution(arr1):
    arr2 =[]
    valid = 1
    for i in arr1:
        if (i != None):
            arr2.append(i)
            valid = i
        else:
            arr2.append(valid)
    print(arr2)
    return arr2
arr3 = [1,None,2,3,None,None,5,None,None,6]
mysolution(arr3)


    

