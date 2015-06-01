def fibonacci_sequence(start_number, end_number):
    a, b = start_number, start_number + 1
    yield a
    yield b
    while a < end_number:
        a, b = b, a + b
        yield b

def sum_of_even_fibonacci_numbers(start_number, end_number):
    total = 0
    for number in fibonacci_sequence(start_number, end_number):
        if number % 2 == 0:
            total += number
    return total

result = sum_of_even_fibonacci_numbers(1, 4000000)
print "\nThe sum of the even-valued terms is: ", result, "\n"
