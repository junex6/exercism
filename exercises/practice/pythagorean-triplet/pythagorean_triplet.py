def triplets_with_sum(number):
    triplets = []
    
    for a in range(1, (number - 1) // 3 + 1):
        numerator = number * number - 2 * number * a
        denominator = 2 * (number - a)
        if numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b
            if a < b < c:
                triplets.append([a, b, c])

    return triplets
