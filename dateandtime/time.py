from datetime import datetime
today = datetime

print(today.now()) #it will return both date and time and ms also

#to check current time without returning date

t = datetime.time(datetime.now())
print("the time now is",t)

#to return date only we can use
d = datetime.date(datetime.now())
print("the date is",d)