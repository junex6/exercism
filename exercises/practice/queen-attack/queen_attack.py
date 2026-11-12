class Queen:
    def __init__(self, row, column):
        self.row = self._check_location(row, "row")
        self.column = self._check_location(column, "column")

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        return (
            self.row == another_queen.row or
            self.column == another_queen.column or
            abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
        )
        
    @staticmethod
    def _check_location(index, name):
        if index < 0:
            raise ValueError(f"{name} not positive")
        if index > 7:
            raise ValueError(f"{name} not on board")
        return index
