#Swap two numbers without using a third variable


x = int(input("Enter x : "))
y = int(input("Enter y : "))
x = x + y   
y = x - y   
x = x - y   
print("After Swapping: x = " ,x, " y =", y)