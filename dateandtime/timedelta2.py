from datetime import datetime
from datetime import timedelta

today = datetime.now() + timedelta(days=10)

def formattime(x):
    y = x.strftime("%A, %B %d, %Y")
    return y


#print(str(today+timedelta(days=10))) #it will display all the details but for 10 days more than today

x = datetime.now() - timedelta(weeks=2)

print(formattime(x))
formattime(today)
