#Calculate lcm of 2 numbers

x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

if x > y:
    z = x
else:
    z = y
while(True):
    if((z % x == 0) and (z % y == 0)):
        lcm = z
        break
    z += 1
print(lcm)

