from datetime import datetime

today = datetime.now()

print(today.strftime("%c")) #it will print day date time and year

print(today.strftime("%x"))  #it will print date

print(today.strftime("%X")) #it will print time

print(today.strftime("%I:%M:%S %p"))