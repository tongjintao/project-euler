"""
Problem Project Euler 4 Description
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalin(n):
	string = str(n)
	for i in range(0,(len(string)+1)//2):
		if string[i] != string[len(string)-i-1]:
			return False
	return True

list = []
products = []

for i in range(100,1000):
	for j in range(100,1000):
		list.append((i,j))
		products.append(i*j)

palins = []

for product in products:
	if isPalin(product):
		palins.append(product)

print max(palins)






	

