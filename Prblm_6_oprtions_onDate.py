
import  datetime
from datetime import date


startDate=input("enter the date in yyyy-mm-dd format :")
Syear,Smonth,Sday=map(int,startDate.split('-'))
date1=datetime.datetime(Syear,Smonth,Sday)


endDate=input("enter the date in yyyy-mm-dd format :")
Eyear,Emonth,Eday=map(int,endDate.split('-'))
date2=datetime.datetime(Eyear,Emonth,Eday)


date3=date2-date1
print(date3.days)

# if(Eyear==Syear):
#     print("true")
# if (Eyear > Syear):
#     print()
# if(Eyear < Syear):
#     print()
#

#print("year=%d month=%d day=%d"%(year,month,day))

