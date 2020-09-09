#Random exercises

#1.Write a Python program to print the following string .
'''
Hey ! I learnt Python ,
    What about you ?
        Better to be early .
'''
print("Hey ! I learnt Python ,\n\tWhat about you ?\n\t\tBetter to be early .")

#2.Write a Python program to get the Python version you are using.

import sys
print("python version :",sys.version )

#3.Write a Python program to display the current date and time.

import datetime
print(datetime.datetime.now())

#4.Write a Python program to accept a filename from the user and print the extension of that.

str1 = "brinda.py"
str2 = str1.split('.')
print("File extension is ",str2[-1])

#5.Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

print(enumerate.__doc__)
print(filter.__doc__)
print(range.__doc__)

#6.Write a Python program to print the calendar of a given month and year.

import calendar

yy = 2020 
mm = 9    
print(calendar.month(yy, mm))

#7.Write a Python program to calculate number of days between two dates.

from datetime import date
startdate = date(2020,1,20)
enddate = date(2020,3,15)
diff = enddate - startdate 
print("difference between dates are  " , diff.days,"days")

#Output (difference between dates are   55 days)