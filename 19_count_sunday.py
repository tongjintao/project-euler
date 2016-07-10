"""
Project Euler 19: Find how many Sundays fell on the first of the month during the twentieth century.
"""

import datetime

sum = 0

for year in range(1901, 2001):
	for month in range(1, 13):
		if datetime.date(year, month, 1).weekday() == 6:
			sum += 1

print sum