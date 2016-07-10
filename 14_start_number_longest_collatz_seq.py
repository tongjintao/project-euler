"""
Project Euler 14: Find the starting number, under one million, that produces the longest Collatz sequence.
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

dcollatz = {}

def collatz(n):	
	list =[]
	if n in dcollatz:
		return dcollatz[n]
	list.append(n)

	while n != 1:
		if n%2==0:
			n = n/2
		else:
			n = 3 * n +1
		if n in dcollatz:
			return list + dcollatz[n]
		list.append(n)
	dcollatz[n] = list
	return list

max_number_of_chain = 1
max_start_number = 1

for i in range(1,1000000):
	clist = collatz(i)
	print i, clist, len(clist)
	if len(clist) > max_number_of_chain:
		max_number_of_chain = len(clist)
		max_start_number = i


print max_number_of_chain, max_start_number





