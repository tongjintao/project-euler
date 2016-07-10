"""
Project Euler 25: Find the first term in the Fibonacci sequence to contain 1000 digits
"""

import sys
import util

fibonacciNumbers = {}

i = 1

while True:
	if util.find_digit(util.fibonacci_number(i)) >= 1000:
		print i
		break
	print i
	i += 1