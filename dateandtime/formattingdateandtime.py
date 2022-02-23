from datetime import datetime
'''
     strftime is used to format date and time
        it is used to format date and time into readable strings.
        it takes one parameter format to specify the format of returning string
    
    formatitng day and date
    Directive           Description
    %a                  weekday short version i.e mon
    %A                  weekday full version i.e monday
    %w                  weekday index numbers 0-6  starting from 0 that is monday
    %d                  day of the month 1-31
    %b                  month name shortversion
    %B                  month name full version
    %m                  month number 1-12
    %y                  year short version without century
    $Y                  year version with century
    
    formatting time
    Directive           Description
    %H                  hour 0-23
    %I                  hour 0-12
    %p                  AM|PM
    %M                  minute 0-59
    %S                  seconds 00-58
    %f                  micro seconds 000000-999999
    %z                  utc offset
    %Z                  timezone
    %J                  day number of the year 001-366
    %U                  weeknumber of the year 00-53 when sunday is the first day of the week
    %W                  weeknumber of the year 00-53 when monday is the first day of the week
    %c                  local version of date and time
    %x                  local version of date
    %X                  local version of time
    %%                  A% character
'''

var = datetime.now()

print(var.strftime("%A"),",",var.strftime("%d"),var.strftime("%B")) # this will return the full version of today's day