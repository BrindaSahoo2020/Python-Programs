#Program to calculate Electricity Bill
'''
1 to 100 units – Rs. 10/unit
100 to 200 units – Rs. 15/unit
200 to 300 units – Rs. 20/unit
above 300 units – Rs. 25/unit
User consumed 350 units
'''

units = int(input("Enter the units consumed : "))
if (units <= 100):       
    total = units * 10 
    print("Electricity bill paid : ",total,"Rs")    
elif (units <= 200): 
    total = ((100 * 10) + (units - 100) * 15)
    print("Electricity bill paid : ",total,"Rs")  
elif (units <= 300): 
    total = ((100 * 10) + (100 * 15) + (units - 200) * 20) 
    print("Electricity bill paid : ",total,"Rs")  
else : 
    total = ((100 * 10) + (100 * 15) + (100 * 20) + (units - 300) * 25)
    print("Electricity bill paid : ",total,"Rs") 

#Output (Electricity bill paid :  5750 Rs)
