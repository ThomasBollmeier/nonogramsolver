from nonogram.puzzle import Puzzle

if __name__ == '__main__':

    puzzle = Puzzle(width=5, height=5)

    puzzle.set_row_segments(0, [1, 1])
    puzzle.set_row_segments(1, [1, 1])
    puzzle.set_row_segments(2, [1])
    puzzle.set_row_segments(3, [1, 1])
    puzzle.set_row_segments(4, [1, 1])

    puzzle.set_column_segments(0, [1, 1])
    puzzle.set_column_segments(1, [1, 1])
    puzzle.set_column_segments(2, [1])
    puzzle.set_column_segments(3, [1, 1])
    puzzle.set_column_segments(4, [1, 1])

    if puzzle.solve():
        puzzle.print()




