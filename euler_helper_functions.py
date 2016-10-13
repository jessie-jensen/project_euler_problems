def prime_factorization(n):
    '''function that returns a list of prime factors of a given number'''
    prime_factors = []
    i = 2
    
    while (n > 1):
        while (n % i == 0):
            prime_factors.append(i)
            n = n / i
        i += 1
    
    return prime_factors



def n_primes(n):
    '''function that returns a list of the first n primes'''
    primes = []
    i = 2

    while (len(primes) < n):
        if len(prime_factorization(i)) == 1:
            primes.append(i)
        i += 1

    return primes