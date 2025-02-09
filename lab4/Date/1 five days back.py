import datetime
time = datetime.datetime.now()
print("Today: "+str(time))
day = datetime.timedelta(days=1)
time -= day*5
print("5 days ago: "+str(time))

print("\nOR another way is")

time2 = datetime.datetime.now()
print("Today's date: "+time2.strftime("%d.%m.%Y"))
time2 -= 5*day
print("5 days ago: "+time2.strftime("%d.%m.%Y"))