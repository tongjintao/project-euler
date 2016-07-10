"""
Project Euler 17: Count how many letters would be needed to write all the numbers in words from 1 to 1000.
"""

numberLetter = {}

numberLetter[1] = 'one'
numberLetter[2] = 'two'
numberLetter[3] = 'three'
numberLetter[4] = 'four'
numberLetter[5] = 'five'
numberLetter[6] = 'six'
numberLetter[7] = 'seven'
numberLetter[8] = 'eight'
numberLetter[9] = 'nine'
numberLetter[10] = 'ten'

sum1to9 = 0

for i in range(1,10):
	sum1to9 += len(numberLetter[i])

print sum1to9

numberLetter[11] = 'eleven'
numberLetter[12] = 'twelve'
numberLetter[13] = 'thirteen'
numberLetter[14] = 'fourteen'
numberLetter[15] = 'fifteen'
numberLetter[16] = 'sixteen'
numberLetter[17] = 'seventeen'
numberLetter[18] = 'eighteen'
numberLetter[19] = 'nineteen'
numberLetter[20] = 'twenty'

sum10to19 = 0

for i in range(10,20):
	sum10to19 += len(numberLetter[i])

print sum10to19

numberLetter[30] = 'thirty'
numberLetter[40] = 'forty'
numberLetter[50] = 'fifty'
numberLetter[60] = 'sixty'
numberLetter[70] = 'seventy'
numberLetter[80] = 'eighty'
numberLetter[90] = 'ninety'

sum20to99 = 0

for i in range(2,10):
	sum = len(numberLetter[i*10]) * 10 + sum1to9
	sum20to99 += sum

print sum20to99

sum100to999 = 0

for i in range(1,10):
	sum = (len(numberLetter[i]) + len('hundred') ) * 100 + len('and') * 99 + sum1to9 + sum10to19 + sum20to99
	sum100to999 += sum

print sum1to9 + sum10to19 + sum20to99 + sum100to999 + len('onethousand')


numberLetter[100] = 'hundred'


