"""Project Euler 9: Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

import math

for i in range(1, 999):
	for j in range(1,999):
		#print i+j+math.sqrt(i*i+j*j)
		if i+j+math.sqrt(i*i+j*j)==1000:
			print "i: ", i, " j: ", j
			print "k: ", math.sqrt(i*i+j*j)
			print "product: ", i*j*math.sqrt(i*i+j*j)



