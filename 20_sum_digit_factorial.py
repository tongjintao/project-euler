"""
Project Euler 20: Find the sum of the digits in 100!
"""

import util

def sumDigit(n):
	if n <10:
		return n
	else:
		return n%10 + sumDigit(n//10)

n = 100

print sumDigit(util.factorial(n))