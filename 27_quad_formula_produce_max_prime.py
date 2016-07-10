"""
Project Euler 27: Find a quadratic formula that produces the maximum number of primes for consecutive values of n
"""

def isPrime(n):
	if n%2==0:
		return False

	for i in range(3, int(n**0.5)+1,2):
		if n%i == 0:
			return False

	return True

max_num_prime = 0
max_a_b = (0,0)

limit = 1000

for a in range(-limit,limit):
	for b in range(-limit,limit):
		n = 0
		quadratic_solution = n ** 2 + a * n + b
		
		print "a = ", a, " b = ", b
		
		tmp_consecutive_prime = set()

		while quadratic_solution >1 and isPrime(quadratic_solution):
			tmp_consecutive_prime.add(quadratic_solution)
			n += 1
			quadratic_solution = n ** 2 + a * n + b

		if len(tmp_consecutive_prime) > max_num_prime:
			max_num_prime = len(tmp_consecutive_prime)
			max_a_b = (a,b)

		print tmp_consecutive_prime


print max_a_b

