"""
Not yet finished
"""


def prime_sieve(n):
	sieve = [True] * (n/2)
	for i in xrange(3,int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def main():
	prime_below_1m = prime_sieve(10000)
	truncated_prime_below_1m = []
	forbid_digit = '245680'
	forbid_digit_tails = '19'
	for prime in prime_below_1m:
		if any(digit in forbid_digit for digit in str(prime)):
			pass
		elif str(prime)[0] in forbid_digit_tails or str(prime)[-1] in forbid_digit_tails:
			pass
		else:
			truncated_prime_below_1m.append(prime)
	print truncated_prime_below_1m


if __name__ == '__main__':
	main()