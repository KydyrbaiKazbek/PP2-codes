from datetime import datetime, timedelta
print(dir(timedelta))
d,m,y = map(int, input("Enter the first date (dd/mm/yyyy): ").split("/"))
time1 = datetime(day = d, month = m, year=y)
d,m,y = map(int, input("Enter the first date (dd/mm/yyyy): ").split("/"))
time2 = datetime(day = d, month = m, year=y)
x = time2-time1
print(x.total_seconds())

