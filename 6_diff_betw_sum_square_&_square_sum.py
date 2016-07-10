"""Project Euler 6: Find the difference between the sum of the squares and the square of the sum
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def sumSquare(n):
	return reduce(lambda x,y: x+y, [i*i for i in range(1,n+1)])

def squareSum(n):
	sum = reduce(lambda x,y: x+y, [i for i in range(1,n+1)])
	return sum*sum

print squareSum(100) - sumSquare(100)