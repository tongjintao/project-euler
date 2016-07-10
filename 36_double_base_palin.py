"""
Project Euler 36: Find the sum of all numbers less than one million, which are palindromic in both base 10 and base 2
"""

def convertToBinary(n):
	if n == 1:
		return '1'
	elif n == 0:
		return
	else:
		return convertToBinary(n//2) + str(n%2)

def isPalin(n):
	for j in range(0, (len(n)+1)//2):
		if n[j] != n[len(n)-1-j]:
			return False
	return True

def main():
	sum_all_double_base = 0

	for i in range(1,1000000):
		s_base10 = str(i)		
		s_base2 = convertToBinary(i)
		
		if isPalin(s_base10) and isPalin(s_base2):
			print i
			sum_all_double_base += i

	print sum_all_double_base


if __name__ == '__main__':
	main()