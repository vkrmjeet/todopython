import calendar
'''
    this script prints the date and month of first friday every month for a meeting
 '''
print("Team Meeting will be on :")
for m in range(1,13):
    cal = calendar.monthcalendar(2022,m)
    week1 = cal[0]
    week2 = cal[1]

    if week1[calendar.FRIDAY]!=0:
        meeting = week1[calendar.FRIDAY]
    else:
        meeting = week2[calendar.FRIDAY]
    print("%10s %d " % (calendar.month_name[m],meeting))
