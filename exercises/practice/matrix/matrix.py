class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for line in matrix_string.splitlines():
            self.matrix.append([int(x) for x in line.split()])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        columns = list(zip(*self.matrix))
        return list(columns[index-1])
