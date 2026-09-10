def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')

    if number == 1:
        return 'deficient'

    aliquot_sum = 1
    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            aliquot_sum += num
            partner = number // num
            if partner != num:
                aliquot_sum += partner
            
    if aliquot_sum == number:
        return 'perfect'
    if aliquot_sum > number:
        return 'abundant'
    return 'deficient'
