from math import sqrt



def gcd(a, b):
    """
    Compute the greatest common divisor of a and b. 
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a

def lcm(a, b): 
    """
    Compute the least common multiple of a and b. 
    """
    return a // gcd(a, b) * b

def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. 

    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]

def primefactors(n):
    """
    Return a list of prime factors of n
    """
    i=2
    primefactors = []
    while i*i <= n:
        if n%i == 0:
            primefactors.append(i)
            n = n // i
        else:
            i += 1

    if n > 1:
        primefactors.append(n)
    return primefactors

def d(n):
    sum = 1
    t = sqrt(n)
    # only proper divisors; start from 2.
    for i in range(2, int(t)+1):
        if n % i == 0:
            sum += i + n / i
    # don't count the square root twice!
    if t == int(t):
        sum -= t
    return sum

def factors(n):    
    """
    Return a list of factors of n. May not be fast
    """
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def factors_fast(n):    
    """
    Return a list of factors of n. From dreamshire.com
    """
    f, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
    if n < 1:
        return []
    while True:
        for gap in ([1, 1, 2, 2, 4] if f < 11 else prime_gaps):
            f += gap
            if f * f > n:  # If f > sqrt(n)
                if n == 1:
                    return factors
                else:
                    return factors + [(n, 1)]
            if not n % f:
                e = 1
                n //= f
                while not n % f:
                    n //= f
                    e += 1
                factors.append((f, e))

def trianglar(n):
    """
    Return nth trianglar number
    """
    return sum ( [ i for i in range(1, n + 1) ] )

def fibonacci_number(n):
    a,b = 1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

def find_digit(n):
    return len(str(n))

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
