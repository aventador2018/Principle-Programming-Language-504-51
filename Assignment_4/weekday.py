import sys
import calendar

year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])

print calendar.day_name[calendar.weekday(year, month, day)]