
###***  D  A  T  E  S ***###
from  datetime import datetime

now = datetime.now()

#& *** imprimiendo el datetime *** &#
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


timestamp = now.timestamp() # formmato POSIX
print(timestamp)

year_2023 = datetime(2023, 1, 1)
print_date(year_2023)

#& *** imprimiendo el time *** &#
from datetime import time

current_time = time(16,35, 0)

print(current_time.hour)    # 0
print(current_time.minute)     # 00:00:00
print(current_time.second)  # 0

#& *** imprimiendo el date *** &#
from datetime import date

current_date = date.today()

print(current_date.year)    # 2023
print(current_date.month)   # 06
print(current_date.day)     # 27

current_date = date(2022, 10, 6)

print(current_date.year)    # 2022
print(current_date.month)   # 10
print(current_date.day)     # 6

#& *** modificando fechas *** &#
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

diff = year_2023 - now # -178 days, 6:32:43.184747
print(diff)

diff = year_2023.date() - current_date # 56 days, 0:00:00
print(diff)

#& *** importando timedelta *** &#
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)  # 121 days, 0:00:00
print(end_timedelta + start_timedelta)  # 661 days, 0:03:20.000200
