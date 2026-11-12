# from itertools import zip_longest

def transpose(text):
    if not text:
        return ""
        
    lines = text.splitlines()

    # Built-in tool can replace entire grid initialization
    # and handle grid transpositions natively
    
    # transposed = zip_longest(*lines, fillvalue="$")
    
    width = len(lines)
    height = max(len(row) for row in lines)
    
    padded = [row.ljust(height, "$") for row in lines]
    transposed = [["$" for _ in range(width)] for _ in range(height)]
    
    for i_row, row in enumerate(padded):
        for i_col, char in enumerate(row):
            transposed[i_col][i_row] = char
    
    return "\n".join(
        "".join(row).rstrip("$").replace("$", " ")
        for row in transposed
    )
