def square_of_sum(number):
    """Calculates the square of the sum of the first n natural numbers: sum(range(number+1)) ** 2"""
    return (number * (number + 1) / 2) ** 2


def sum_of_squares(number):
    """Calculates the sum of the squares of the first n natural numbers: sum([x ** 2 for x in range(number+1)])"""
    return number * (number + 1) * (2 * number + 1) / 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
