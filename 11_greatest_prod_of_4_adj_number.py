"""Project Euler 11: Find the greatest product of four adjacent numbers in the same direction in a grid
"""

import re

def out_of_range(i, j):
	if i >= 20 or  j >= 20:
		return True
	else:
		return False

f = open('11_matrix_20x20.txt', 'r')
content = f.read()
content = re.sub('\n', ' ', content)
numbers = content.split(" ")

n=20

grid = [numbers[i:i+n] for i in range(0, len(numbers),n)]

directions = [(1,0), (0,1),(1,1),(1,-1)]

max = 1

for row in range(0,20):
	for column in range(0,20):
		for direction in directions:
			productList = []
			productList.append(int(grid[row][column]))
			for i in range(1,4):
				if not out_of_range(row+i*direction[0], column+i*direction[1]):
					productList.append(int(grid[row+i*direction[0]][column+i*direction[1]]))
			if len(productList) == 4  and 0 not in productList:
				product = reduce(lambda x,y:x*y, productList)
				if product > max:
					max = product

print max