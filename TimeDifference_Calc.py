#Python program to find difference between an employee login and logout time in Office

from datetime import datetime, time

login = "9:10:20 AM"
logout = "02:23:10 PM"

def convert24(str1):   
#Checking if last two elements of time is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12":
        return ("00" + str1[2:-2])        
#Remove the AM     
    elif str1[-2:] == "AM":
        return (str1[:-2]) 
#Checking if last two elements of time is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return (str1[:-2])    
    else:      
#Add 12 to hours and remove PM 
        return (str(int(str1[:2]) + 12) + str1[2:8])

ob1 = convert24(login)
ob2 = convert24(logout)
print ("login = " ,ob1)
print ("logout = " ,ob2)

x = datetime.strptime('14:23:10', '%H:%M:%S')
y = datetime.strptime('9:10:20', '%H:%M:%S')

diff = x - y
print("Working hour of the employee inside office is : ",diff)

#Output
'''
login =  9:10:20 
logout =  14:23:10
Working hour of the employee inside office is :  5:12:50
'''