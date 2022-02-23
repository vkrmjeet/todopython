'''
     calender module can be used to work with dates
     it can also be used in text and html based calendars
'''

import calendar
#cal = calendar.TextCalendar(calendar.MONDAY) this will generate a text calendar
cal = calendar.HTMLCalendar(calendar.MONDAY)

str = cal.formatmonth(2022,4)

print(str)