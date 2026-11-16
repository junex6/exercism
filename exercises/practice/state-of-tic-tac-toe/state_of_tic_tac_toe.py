def gamestate(board):
    # Flatten board
    marks = [mark for row in board for mark in row]
    
    count_X = marks.count("X")
    count_O = marks.count("O")

    # Validate turn order (X goes first)
    if count_O > count_X:
        raise ValueError("Wrong turn order: O started")

    if count_X - count_O == 2:
        raise ValueError("Wrong turn order: X went twice")

    def _win(player):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        return any(all(marks[i] == player for i in win) for win in wins)
    
    win_X = _win("X")
    win_O = _win("O")

    # Validate impossible game states
    if (win_X and win_O) or (win_X and count_O >= count_X) or (win_O and count_X > count_O):
        raise ValueError("Impossible board: game should have ended after the game was won")

    if win_X or win_O:
        return "win"

    if count_X + count_O == 9:
        return "draw"
    
    return "ongoing"
