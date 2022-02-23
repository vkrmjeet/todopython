from datetime import date
#there are many advanced function that can be used
today = date.today()
print("the weekday number is",today.weekday()) #0n monday it will return 0

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

day = today.weekday()

print("the weekday is",days[day]) #this will return the name of the day today