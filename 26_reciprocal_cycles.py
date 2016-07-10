"""
Project Euler 26: Find the value of d < 1000 for which 1/d contains the longest recurring cycle
"""

def findRecurringDigit(divisor):
	digitList = []
	dividend = 1

	# find the recurring reminder instead of the quotient
	while True:
		reminder = dividend % divisor
		
		if reminder == 0:
			del digitList[:]
			break

		if reminder in digitList:
			index = digitList.index(reminder)
			digitList = digitList[index:]
			break

		digitList.append(reminder)
		dividend = reminder * 10

	return len(digitList)

max_cycle = (0,0)

for i in range(3,1000,2):
	recurringDigit = findRecurringDigit(i)
	if recurringDigit > max_cycle[1]:
		max_cycle = (i, recurringDigit)

print max_cycle[0]


