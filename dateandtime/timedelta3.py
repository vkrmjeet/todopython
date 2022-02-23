from datetime import datetime
from datetime import timedelta

daysahead = datetime.today()

xmas = datetime(daysahead.year,12,25)

timetoxmas = xmas - daysahead

print(timetoxmas.days,timetoxmas.)