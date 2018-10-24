#!/usr/bin/env python3

# Calculating future times
from datetime import datetime, timedelta

now = datetime.now()

testDate = now + timedelta(days=2) # 2 days from now
treeWeeksAgo = now - timedelta(weeks=3)

# print(f"Daqui a dois dias: {testDate.date()}") # it's a datetime instance
# print()
#
# print(f"Tree weeks ago: {treeWeeksAgo.date()}")
# print()


# Using calendar library
import calendar

# cal = calendar.month(2018,10)  # October 2001
# print(cal)
#
# cal2 = calendar.weekday(2018, 10, 24)  # What's 11 weekday
# print(cal2)

print()
# leap year/bissextile year
# print(calendar.isleap(1999))
# print(calendar.isleap(2000))
# print(calendar.isleap(2018))

