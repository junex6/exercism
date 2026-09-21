def sum_of_multiples(limit, multiples):
    energy_points = {
        value
        for item in multiples if item > 0
        for value in range(item, limit, item)
    }
    return sum(energy_points)
