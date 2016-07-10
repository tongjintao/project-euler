"""
Project Euler 35: Find the number of circular primes below one million
"""

from re import search
import util

L = 1000000

#return a list of rotations for string s
def rotate(s):
    return [s[n:] + s[:n] for n in range(1, len(s))]

#make a set of primes < L and remove any that have {0,2,4,5,6,8} except 2 and 5
primes = set(['2','5']+[str(p) for p in util.prime_sieve(L) if not search('[024568]', str(p))])

for p in primes:
	if all(pr in primes for pr in rotate(p)):
		print p


n_circular_primes = sum(all(pr in primes for pr in rotate(p)) for p in primes)
print "Project Euler 35 Solution =", n_circular_primes

