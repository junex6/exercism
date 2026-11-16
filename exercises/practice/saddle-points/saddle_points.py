def saddle_points(matrix):
    if len({len(row) for row in matrix}) > 1:
        raise ValueError("irregular matrix")

    row_maxes = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]

    return [
        {"row": r+1, "column": c+1}
        for r, row in enumerate(matrix)
        for c, val in enumerate(row)
        if val == row_maxes[r] and val == col_mins[c]
    ]
