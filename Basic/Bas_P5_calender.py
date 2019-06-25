import calendar

def getCalender(month,year):
 m=int(month)
 y=int(1993)
 print(calendar.month(y, m))
 calendar.monthrange()


month=input("enter value of month :")
year=input("enter value of Year :")
getCalender(month,year)
#print(calendar.calendar(2019))