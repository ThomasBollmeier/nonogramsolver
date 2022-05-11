class CellState:
    UNKNOWN = 1
    FILLED = 2
    EMPTY = 3


class Board(object):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[CellState.EMPTY for col in range(self.width)]
                      for row in range(self.height)]

    def set_cell(self, row, col, state):
        self.cells[row][col] = state

    def get_cell(self, row, col):
        return self.cells[row][col]
