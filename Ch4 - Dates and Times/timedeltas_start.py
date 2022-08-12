#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date, timedelta
from datetime import time
from datetime import datetime
from turtle import st


# TODO: construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=3))

# TODO: print today's date
now=datetime.now()
print("today is :" , now)

# TODO: print today's date one year from now
print("one year from now it will be" ,str(now+timedelta(days=365)))

# TODO: create a timedelta that uses more than one argument
print("in two weeks and 3 days  it will be" ,str(now+timedelta(weeks=2,days=3)))

# TODO: calculate the date 1 week ago, formatted as a string
t=datetime.now()-timedelta(weeks=1)
print("a week ago : " , t.strftime("%A  %d:%B,%Y"))
### How many days until April Fools' Day?
print("datetime time : ",datetime(2019,4,1))
print("date time : ",date(2019,4,1))

tday=date.today()
print("tday : ",tday)
afd=date(tday.year,4,1)
print("afd : ",afd)

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd<tday:
    print("april fools day already went by : ",(tday-afd).days )# tday-afd▶133 days, 0:00:00
    afd=afd.replace(year=tday.year+1)
# TODO: Now calculate the amount of time until April Fool's Day  
time_to_april=afd-tday
print("it is ",time_to_april.days,"days until the next april fools day")
