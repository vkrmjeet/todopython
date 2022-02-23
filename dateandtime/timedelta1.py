'''
     we can perform time calaculations with the help of timedelta object
     it belongs to the time module
     it is used to perform calculations based on time and date.
'''
from datetime import datetime
from datetime import timedelta

today = datetime.now()

print(str(today + timedelta(365)))  #it will give current time after 365 days

print(timedelta(days=365,hours=7,minutes=5))