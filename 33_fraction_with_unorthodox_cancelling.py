"""
Project Euler 33: Discover all the fractions with an unorthodox cancelling method.
"""

den_product = 1
nom_product = 1

for i in range(1,10):
	for den in range(1, i):
		for nom in range(1, den):
			if (nom * 10 + i) * den == nom * (i * 10 + den):
				den_product *= den
				nom_product *= nom


