#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project Euler 23: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number whose proper divisors are less than the number is called deficient and a number whose proper divisors exceed the number is called abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import util


limit = 20162
sum = 0
# it's a set, after all. sets are faster than lists for our needs.
abn = set()
for n in range(1, limit):
    if util.d(n) > n:
        abn.add(n)
    # if the difference of the number we're examining and every number in the set
    # is in the set, then the number is the sum of two abundant numbers.
    # otherwise, we must add it to our sum in question.
    if not any( (n-a in abn) for a in abn ):
        sum += n