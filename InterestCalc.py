#Python Program for calculation of interests
#Sample Input 
'''
P = 10000
T = 5
R = 8.2 
'''
#Sample Output
'''
Simple Interest is : 4099.999999999999 Rs
Compound Interest is : 14829.834482784325 Rs
'''
P = float(input("Enter principle amount Rs  : "))
T = int(input("Enter Tenure  : "))
R = float(input("Enter rate of interest  : "))

si = (P*T*R)/100
ci = P * (pow((1 + R / 100), T)) 

print("Simple Interest is : ",si,"Rs")
print("Compound Interest is : ",ci,"Rs")