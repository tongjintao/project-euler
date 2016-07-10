"""
Project Euler 34: Find the sum of all numbers which are equal to the sum of the factorial of their digits
"""

import util

sum_all_valid_number = 0

for i in range(11,409114):
	digit = list(str(i))
	sum_factorial = 0
	for j in range(0,len(digit)):
		sum_factorial += util.factorial(int(digit[j]))
	if sum_factorial == i:
		print i
		sum_all_valid_number += i

print sum_all_valid_number

