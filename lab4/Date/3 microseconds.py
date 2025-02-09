from datetime import datetime, timedelta
time = datetime.now()
micros = timedelta(microseconds = time.microsecond)
print(time)
print(micros)
time-=micros
print(time)

print("\nOr another method is replace")
time2 = datetime.now()
print(time2)
time2 = time2.replace(microsecond = 0)
print(time2)