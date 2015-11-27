def is_prime(n):
    for i in xrange(2, n-1):
        if n % i == 0:
            return False
    return True


def list_primes(n):
    return [x for x in xrange(2, n) if is_prime(x)]


def list_prime_factors(n):
    pl = list_primes(n)
    pl2 = [x for x in pl if x * x < n]
    return [x for x in pl2 if n % x == 0]


def largest_prime_factor(n):
    return max(list_prime_factors(n))