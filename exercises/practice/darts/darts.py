def score(x, y):
    """Calculate the score of a dart throw given its (x, y) coordinates.
    - Inner circle (radius <= 1): 10 points
    - Middle circle (radius <= 5): 5 points
    - Outer circle (radius <= 10): 1 point
    - Outside the target: 0 points
    """
    d_squared = x * x + y * y

    if d_squared <= 1:
        return 10
    if d_squared <= 25:
        return 5
    if d_squared <= 100:
        return 1
    return 0
