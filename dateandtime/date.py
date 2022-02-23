from datetime import date
# these are all the classes that are imported from the datetime package
#the error is because the file is named as datetime and the package is of samename and python tries to check if there
#are modules of the same name exists thats why always check the file name

#check today's date
print(date.today())  #this print today's date

#there is one more method you can use
today = date.today()
print("today is",today) #the working is still the same we have just reassigned the class and its function to a variable
#we can also use specific date components
print(today.day) # this will return the day
print(today.month) #this will print the month
print(today.year) #this will print the year
#or we can use the in one single statement

print("the component of date are",today.day,"/",today.month,"/",today.year)