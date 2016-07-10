"""
Project Euler 22: Calculate the total of all the name scores in the file of first names
Using 22_names.txt (right click and Save Link/Target As), 
a 46k text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

import pickle

f = open('22_names.txt', 'rb')
names = f.read().split(",")
f.close()

nameDic = {}
sum = 0

names.sort()

for index, name in enumerate(names):
	name = name.replace("\"", "")
	value = 0
	for character in name:
		value += ord(character) - 64
	sum += value * (index +1)
	print name, ": ", value, " * ", index

print sum
	


