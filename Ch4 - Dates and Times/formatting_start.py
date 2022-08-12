#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now=datetime.now()
    print("now : ",now)
    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print("str time format term of lower case",now.strftime("%a,%d,%b,%y"))
    print("str time format term of upper case",now.strftime("%A,%d,%B,%Y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print("current local time and date ",now.strftime('%c'))
    print("local date ",now.strftime('%x'))
    print("local time  ",now.strftime('%X'))

    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print("current time : ",now.strftime("%I:%M:%S  %p"))
#https://docs.python.org/3/library/datetime.html
if __name__ == "__main__":
    main()
