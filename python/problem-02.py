def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


def sum_even_fibonacci(n):
    return sum(x for x in fibonacci(n) if not x % 2)

print(sum_even_fibonacci(4000000))
