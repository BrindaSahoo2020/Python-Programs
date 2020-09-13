#Calculate lcm of any numbers

x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
z = int(input("Enter 3rd number : "))
max1 = max(x,y,z)

while(True):
    if((max1 % x == 0) and (max1 % y == 0) and (max1 % z == 0)):
        lcm = max1
        break
    max1 += 1
print("LCM is :",lcm)
