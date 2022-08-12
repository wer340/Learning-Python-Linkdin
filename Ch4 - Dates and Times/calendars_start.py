#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar 

# TODO: create a plain text calendar
c=calendar.TextCalendar(calendar.SATURDAY)
str=c.formatmonth(2022,8,0)
print(str)
# TODO: create an HTML formatted calendar
ch=calendar.HTMLCalendar(calendar.SATURDAY)
strh=ch.formatmonth(2022,8,0)
print(strh)

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2022,8 ):
    print(i)
  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("###Team meeting will be in first friday of month each other##")

for i in range(1,13):
    
    month=calendar.monthcalendar(2022,i)
    print(month)
    one_Week=month[0]
    two_Week=month[1]

    if one_Week[calendar.FRIDAY] !=0:
        meetday=one_Week[calendar.FRIDAY]
    else:
        meetday=two_Week[calendar.FRIDAY]
    
    print("month : ",calendar.month_name[i],"#########","day : ",meetday)