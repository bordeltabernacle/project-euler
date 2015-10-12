def sum_mul_three_five(end_num):
    """
    Returns the sum of all the multiples of 3 or 5 below end_num
    """
    return sum([num for num in range(end_num) if not num % 3 or not num % 5])
