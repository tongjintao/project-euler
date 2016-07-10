"""
Project Euler 21: Evaluate the sum of all amicable pairs under 10,000
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time
 
def sum_divisors(n):
    s = 0
    for i in range(1,int(n**0.5)):
        if n % i == 0: 
            s += i
            if i != 1:
                s += n//i
    return s
 
def amicable_pairs_xrange(low,high):
    L = [sum_divisors(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs
 
def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])
 
start = time.time()
 
ans = sum_pairs(amicable_pairs_xrange(1,10000))
 
elapsed = time.time() - start
 
print("%s found in %s seconds") % (ans,elapsed)
