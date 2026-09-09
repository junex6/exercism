def is_armstrong_number(number):
    s = str(number)
    num_digits = len(s)
    return sum(int(digit) ** num_digits for digit in s) == number
