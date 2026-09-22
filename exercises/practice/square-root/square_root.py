def square_root(number):
    """Integer square root (binary search)"""
    if number < 2:
        return number
        
    low = 1                      # lower bound
    high = number // 2           # upper bound

    while low <= high:
        mid = (low + high) // 2  # midpoint
        sq = mid * mid
        
        if sq == number:
            return mid
        elif sq < number:
            low = mid + 1
        else:
            high = mid - 1

    return high
