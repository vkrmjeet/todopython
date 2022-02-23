import calendar

cal = calendar.TextCalendar(calendar.SUNDAY)

'''for days in cal.itermonthdays(2022,1):
    print(days) #it should print days in jan month
'''

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)