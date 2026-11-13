def tick(matrix):
    if not matrix:
        return matrix

    new_matrix = [[cell for cell in row] for row in matrix]
    
    for i_row, row in enumerate(matrix):
        for i_col, cell in enumerate(row):
            
            neighbors = neighbor(matrix, i_row, i_col)
            live_neighbors = sum(neighbors)
            
            if cell == 1:
                if live_neighbors in (2, 3):
                    new_matrix[i_row][i_col] = 1
                else:
                    new_matrix[i_row][i_col] = 0
            else:
                if live_neighbors == 3:
                    new_matrix[i_row][i_col] = 1
                
    return new_matrix

def neighbor(matrix, i_row, i_col):
    cell = matrix[i_row][i_col]
    count = len(matrix)
    neighbors = []

    for row_offset in (-1, 0, 1):
        for col_offset in (-1, 0, 1):
            # skip cell itself
            if row_offset == 0 and col_offset == 0:
                continue
                
            r = i_row + row_offset
            c = i_col + col_offset
            
            if 0 <= r < count and 0 <= c < count:
                neighbors.append(matrix[r][c])
                
    return neighbors
