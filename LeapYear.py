#Python program to find leap year

#Sample Input
'''1996,1998'''
#Sample Output
'''
1996 is a Leap Year
1998 is not a Leap Year
'''
year = int(input("Enter a year : "))
if (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
elif (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")