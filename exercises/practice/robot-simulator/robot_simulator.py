# Globals for the directions
# Change the values as you see fit
NORTH = 0 # y+
EAST = 1  # x+
SOUTH = 2 # y-
WEST = 3  # x-


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)

    def move(self, actions):
        for action in actions:
            if action in {"L", "R"}:
                self.direction = self._turn(action)
            elif action == "A":
                self._adv()

    def _turn(self, move):
        curr_dir = self.direction
        if move == "R":
            curr_dir += 1
        elif move == "L":
            curr_dir -= 1
        
        if curr_dir > 3:
            curr_dir -= 4
        elif curr_dir < 0:
            curr_dir += 4
        return curr_dir

    def _adv(self):
        curr_dir = self.direction
        if curr_dir == NORTH:
            self.y_pos += 1
        if curr_dir == EAST:
            self.x_pos += 1
        if curr_dir == SOUTH:
            self.y_pos -= 1
        if curr_dir == WEST:
            self.x_pos -= 1
