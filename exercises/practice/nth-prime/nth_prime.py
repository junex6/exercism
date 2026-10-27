def _is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # check odd numbers up to the square root of num
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number == 1:
        return 2

    count = 1
    candidate = 3

    while count < number:
        if _is_prime(candidate):
            count += 1
            if count == number:
                return candidate
        candidate += 2 # skip even numbers
