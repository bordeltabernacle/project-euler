def prime(n):
    if n > 2 and n % 2 == 0 or \
       n > 3 and n % 3 == 0 or \
       n > 5 and n % 5 == 0 or \
       n > 7 and n % 7 == 0 or \
       n > 13 and n % 13 == 0:
        pass
    else:
        return n


def largest_prime_factor(n):
    largest = None
    for x in xrange(n):
        if x > 0 and n % int(x) == 0 and prime(x):
            if largest is None or x > largest:
                largest = x
                print largest
    print "Largest is %d" % largest


largest_prime_factor(600851475143)
# largest_prime_factor(13195)
