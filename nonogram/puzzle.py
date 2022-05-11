from nonogram.board import Board, CellState


class Puzzle(object):

    def __init__(self, width, height):
        self.board = Board(width, height)
        self.row_groups = [[0] for _ in range(self.board.height)]
        self.column_groups = [[0] for _ in range(self.board.width)]

    def set_row_segments(self, row, segments):
        self.row_groups[row] = segments

    def set_column_segments(self, col, segments):
        self.column_groups[col] = segments

    def get_row_constraints(self, row):
        filled = set()
        empty = set()
        for col in range(self.board.width):
            state = self.board.get_cell(row, col)
            if state == CellState.FILLED:
                filled.add(col)
            elif state == CellState.EMPTY:
                empty.add(col)
        return filled, empty

    def get_column_constraints(self, col):
        filled = set()
        empty = set()
        for row in range(self.board.height):
            state = self.board.get_cell(row, col)
            if state == CellState.FILLED:
                filled.add(row)
            elif state == CellState.EMPTY:
                empty.add(row)
        return filled, empty
