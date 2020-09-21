#Python Program for How to check if a given number is Fibonacci number?

#Check with your own inputs

n = int(input("Enter the number: "))
x = 0
y = 1
z = 1
if (n == 0 or n == 1):
    print(n, "is a fibonacee number")
else:
    while z < n:
        z = x + y
        y = x
        x = z
    if (z == n):
        print(n, "is a fibonacee number")
    else:
        print(n, "is not a fibonacee number")
