from datetime import date
import time
import datetime

now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
print("To birthday: ", (now - birthday).days)

datetime.datetime.now()
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

print(time.time())

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print((dt + thousandDays).strftime("%Y.%m.%d"))




