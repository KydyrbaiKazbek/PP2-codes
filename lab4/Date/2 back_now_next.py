import datetime 
time = datetime.datetime.now()
day = datetime.timedelta(days=1)
print(f"Yesterday {(time-day).strftime('%d.%m.%Y')}")
print(f"Today {time.strftime('%d.%m.%Y')}")
print(f"Tomorrow {(time+day).strftime('%d.%m.%Y')}")