"""
Project Euler 15: Find the number of routes from the top left corner to the bottom right corner in a rectangular grid.
How many routes are there through a 20x20 grid?
"""

def pascalTriangle(rows):
	"""
	Print out the pascal triangle structure and the max number in each row
	"""
    for rownum in range (rows):
        newValue=1
        PrintingList = [newValue]
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
        print PrintingList, max(PrintingList)
    print 

L = 20
pascalTriangle(L*2+1)