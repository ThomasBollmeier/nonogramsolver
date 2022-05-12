from nonogram.board import Board, CellState
from nonogram.solver import valid_placements


class Puzzle(object):

    def __init__(self, width, height):
        self.board = Board(width, height)
        self.row_groups = [[0] for _ in range(self.board.height)]
        self.column_groups = [[0] for _ in range(self.board.width)]

    def print(self):
        state_char = {
            CellState.UNKNOWN: "?",
            CellState.EMPTY: "-",
            CellState.FILLED: "X",
        }
        for row in range(self.board.height):
            line = ""
            for col in range(self.board.width):
                line += state_char[self.board.get_cell(row, col)]
            print(line)
        print()

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

    def is_solved(self):
        for row in range(self.board.height):
            for col in range(self.board.width):
                if self.board.get_cell(row, col) == CellState.UNKNOWN:
                    return False
        return True

    def solve(self):
        return self.solve_row(0)

    def solve_row(self, row):
        if row >= self.board.height:
            return True # we have reached the end
        groups = self.row_groups[row]
        placements = valid_placements(groups, self.board.width)
        for placement in placements:
            for col in range(self.board.width):
                self.board.set_cell(row, col, CellState.EMPTY)
            for begin, end_excl in placement:
                for col in range(begin, end_excl):
                    self.board.set_cell(row, col, CellState.FILLED)
            if self._is_board_consistent():
                if self.solve_row(row + 1):
                    return True
            for col in range(self.board.width):
                self.board.set_cell(row, col, CellState.UNKNOWN)
        return False

    def _is_board_consistent(self):
        for col in range(self.board.width):
            if not self._col_placement_ok(col):
                return False
        return True

    def _get_placed_column_groups(self, col):
        ret = []
        group = 0
        for row in range(self.board.height):
            state = self.board.get_cell(row, col)
            if state == CellState.UNKNOWN:
                break
            elif state == CellState.FILLED:
                group += 1
            elif state == CellState.EMPTY:
                if group > 0:
                    ret.append(group)
                    group = 0
        if group > 0:
            ret.append(group)
        return ret

    def _col_placement_ok(self, col):
        placed_groups = self._get_placed_column_groups(col)
        num_groups = len(placed_groups)
        required_groups = self.column_groups[col]
        for idx, group in enumerate(placed_groups):
            try:
                required_group = required_groups[idx]
            except IndexError:
                return False
            if idx != num_groups - 1:
                if group != required_group:
                    return False
            else:
                if group > required_group:
                    return False
        return True
