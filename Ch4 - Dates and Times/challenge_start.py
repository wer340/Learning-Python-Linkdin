# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

print("which day of week do you want to count? ")
name_day=[]

for index,name in enumerate(calendar.day_name) :
    print(index ,  ":  ",name )
    name_day.append(name)
print("'exit'  to quit")
while True:

    try:
        num_select=input("enter your number of weekday ? : ")
        if num_select=="exit":
            break
        num_select=int(num_select)
        day_selected=name_day[num_select]
    except:
        continue

    month_select=input("enter your number of month ? : ")
    if month_select=="exit":
        break
    month_select=int(num_select)
    if month_select >= 0 and month_select < 13:
        month_select=name_day[month_select]
    else:
        continue
    
    year_select=input("enter your number of year ? : ")
    if year_select=="exit":
        break
    year_select=int(year_select)
    if year_select > 1800 and month_select < 2400:
        month_select=name_day[month_select]
    else:
        print("too much big")
        continue


