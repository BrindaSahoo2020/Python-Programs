#Python program on Binary Search for a Sorted array

#Sample Input
#45,1000

#Sample Output
#Number is found at index : 3
#Number is not found


l1 = [1,2,7,45,53,100,101,102]
x = int(input("Enter a digit you want to search :"))
l =len(l1)
start = 0
end = l-1
found = False
while start <= end :
	mid = (start + end)//2
	if l1[mid] == x: 
		print("Number is found at index :",mid)
		found = True
		break
	elif x < l1[mid]:
		end = mid-1
	else:
		start = mid+1
if(found == False):
	print("Number is not found")