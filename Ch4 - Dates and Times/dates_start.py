#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import time
from datetime import datetime
from sqlite3 import Date

def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today=date.today()
    print("tody is : ",today)

    # TODO: print out the date's individual components
    print(f" date components :{today.day} ,{today.month},{today.year}")
    
    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("todays weekdays # is ",today.weekday())
    days=["mon","tue","wed","thur","fri","sat","sun"]
    print("todays weekdays # is ",days[today.weekday()])
    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today_d=datetime.now()
    print("today by date time object #### :" ,today_d)
    
    # TODO: Get the current time
    t=datetime.time(datetime.now())
    print("current time is #### : ", t)
 
   
  
if __name__ == "__main__":
    main()
  