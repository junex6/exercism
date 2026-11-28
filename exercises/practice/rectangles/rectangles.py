def rectangles(strings: list[str]) -> int:
    """Count rectangles in an ASCII diagram."""
    if not strings or not strings[0]:
        return 0

    # gather all corners marked "+"
    rows = len(strings)
    
    corners: list[list[int]] = [[] for _ in range(rows)]
    for r, row in enumerate(strings):
        for c, ch in enumerate(row):
            if ch == "+":
                corners[r].append(c)

    # check if two points are connnected horizontally
    def _row_connected(r: int, c1: int, c2: int) -> bool:
        return all(strings[r][c] in {"+", "-"} for c in range(c1+1, c2))

    # check if two points are connected vertically
    def _col_connected(r1: int, r2: int, c: int) -> bool:
        return all(strings[r][c] in {"+", "|"} for r in range(r1+1, r2))

    # count rectangles
    count = 0
    for r1, row in enumerate(corners):
        for i, c1 in enumerate(row):
            for c2 in row[i+1:]:
                if _row_connected(r1, c1, c2):
                    for r2 in range(r1+1, rows):
                        if (
                            c1 in corners[r2] 
                            and c2 in corners[r2]
                            and _col_connected(r1, r2, c1) 
                            and _col_connected(r1, r2, c2) 
                            and _row_connected(r2, c1, c2)
                        ):
                                count += 1

    return count
