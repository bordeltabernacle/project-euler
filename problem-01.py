def sum_mul_three_five(end_num):
    """
    Returns the sum of all the multiples of 3 or 5 below end_num
    """
    total = []
    for num in range(end_num):
        if num % 3 == 0 or num % 5 == 0:
            total.append(num)
    return sum(total)
