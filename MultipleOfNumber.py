#Print first y multiples of x

#Sample Input (x = 2, y = 5)

#Sample Output ([2,4,6,8,10])

#Method1
x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
lst = []
for i in range(1,y+1):
    j = x * i
    lst.append(j)
print(lst)

#Method2
m = 6
n = 3 
a = range(n, (m * n)+1, n)  
print(*a) 

#Output 3 6 9 12 15 18
