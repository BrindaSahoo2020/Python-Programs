#Find yesterday’s, today’s and tomorrow’s date

from datetime import datetime, timedelta 

today = datetime.today()

yesterday = today - timedelta(1) 

tomorrow = today + timedelta(1)

#strftime() is to format date according to the need by converting them to string
print("Today's date is :" ,today.strftime('%d-%m-%Y'))
print("Yesterdays's date is :" ,yesterday.strftime('%d-%m-%Y'))
print("Tomorrow's date is :" ,tomorrow.strftime('%d-%m-%Y'))

#Can calculate any date before or after present date

sevenday_before = today - timedelta(7) 

sevenday_after = today + timedelta(7) 

print("Date after a week is :" ,sevenday_after.strftime('%d-%m-%Y'))
print("Date before a week is :" ,sevenday_before.strftime('%d-%m-%Y'))

#Check with your own inputs