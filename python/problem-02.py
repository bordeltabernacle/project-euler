def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


def sum_even(coll):
    return sum([x for x in coll if x % 2 == 0])


def sum_even_fibonacci(n):
    return sum_even(list(fibonacci(n)))