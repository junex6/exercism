def factors(value):
    if value <= 1:
        return []

    prime_factors = []

    while value % 2 == 0:
        prime_factors.append(2)
        value //= 2

    divisor = 3
    while divisor * divisor <= value:
        while value % divisor == 0:
            prime_factors.append(divisor)
            value //= divisor 
        divisor += 2
        
    if value > 1:
        prime_factors.append(value)
        
    return prime_factors
