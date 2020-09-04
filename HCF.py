#Python program to print highest common factor(HCF)

#Sample Input (11,22,33,34 / 10,8,12,14)

#Sample Output (1 / 2)

n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))
n4 = int(input("Enter 4th number : "))

small = (min(n1,n2,n3,n4))
for i in range(1,small+1):
    if((n1 % i == 0) and (n2 % i == 0) and (n3 %i == 0) and (n4 %i == 0)):
        hcf = i
print("Highest common factor is : ",hcf)
