"""Project Euler 7: Find the 10001st prime number
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

import util

n = 10000
primes_list = util.prime_sieve(110000)
print primes[n]

