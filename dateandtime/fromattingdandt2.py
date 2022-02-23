from datetime import datetime

today = datetime.now()

print(today)

print(today.strftime("the current date is : %d/%m/%Y"))

print(today.strftime("%A, %d %B, %Y"))