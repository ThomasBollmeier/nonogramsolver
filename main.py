from nonogram.solver import valid_placements, determine_filled_empty_sets

if __name__ == '__main__':
    for p in valid_placements([6, 6], 15, filled={0, 14}):
        print(p)