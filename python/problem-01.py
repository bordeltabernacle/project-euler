def sum_mul_three_five(end):
    """
    Returns the sum of all the multiples of 3 or 5 below end_num
    """
    return sum(n for n in range(end) if not n % 3 or not n % 5)
