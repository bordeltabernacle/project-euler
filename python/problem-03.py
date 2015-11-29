def prime_factors(number, factor=2, result=()):
    while factor * factor <= number:
        if number % factor == 0:
            result += (factor,)
            number /= factor
        else:
            factor += 1
    result += (number,)
    return result

print max(prime_factors(600851475143))
