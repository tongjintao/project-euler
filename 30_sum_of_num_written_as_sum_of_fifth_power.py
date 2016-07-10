"""
Project Euler 30: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits
"""

sumFifth = 0

for i in range(1, 354295):
	digitList = [int(digit) for digit in str(i)]
	if i == sum(map(lambda x: x**5, digitList)):
		print i
		sumFifth += i

print sumFifth - 1


