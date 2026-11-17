MAPPING = {
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
    " _ | ||_|   ": "0"
}

def convert(input_grid):
    # when the lines aren't multiples of 4
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # when the columns aren't multiples of 3
    line_len = len(input_grid[0])
    if line_len % 3 != 0 or not all(len(l) == line_len for l in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    num_rows = len(input_grid) // 4
    num_cols = line_len // 3

    result_rows = []
    for r in range(num_rows):
        # extract 4 lines of the current row
        row_lines = input_grid[r*4:(r+1)*4]
        
        row_digits = []
        for c in range(num_cols):
            # extract 3 character slice across 4 lines
            digit_lines = [line[c*3:(c+1)*3] for line in row_lines]
            digit_str = "".join(digit_lines)

            row_digits.append(MAPPING.get(digit_str, "?"))

        result_rows.append("".join(row_digits))

    return ",".join(result_rows)
    

    # input_grid_w_sep_rows = [input_grid[i:i+4] for i in range(0, len(input_grid), 4)]

    # flattened_rows = []
    # for row in input_grid_w_sep_rows:
    #     split_lines = [
    #         [line[i:i+3] for i in range(0, len(line), 3)] for line in row
    #     ]
    #     split_cols = list(zip(*split_lines))
    #     flattened_rows.append(
    #         ["".join(split_col) for split_col in split_cols]
    #     )

    # result = str()
    # num_rows = len(input_grid) // 4
    # for i, row in enumerate(flattened_rows):
    #     for digit in row:
    #         result += MAPPING.get(digit, "?")
    #     if i+1 < num_rows:
    #         result += ","

    # return result
    
    
        
