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
    month_select=int(month_select)
    if month_select > 0 and month_select < 13:
        month=month_select
    else:
        continue
    
    year_select=input("enter your number of year ? : ")
    if year_select=="exit":
        break
    year_select=int(year_select)
    if year_select > 1800 and year_select < 2400:
        year=year_select
    else:
        print("too much big")
        continue
    specific_day=[]
    date_specific_month=calendar.monthcalendar(year,month)
    print("################### ",day_selected.upper()," ",calendar.month_name[month] ," ",year,"###################")
    for week in date_specific_month:
        
        if week[num_select] !=0:
            specific_day.append(week[num_select])
            print(week[num_select] ,calendar.month_name[month]  )
        else:
            print("type : ",type(week[num_select]) ,"week[num_select]  : ",week[num_select] )  

       
    print(specific_day)