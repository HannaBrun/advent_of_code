from itertools import product
from common import parse_file

def run():
    data = parse_file(4)
    grid = data.split('\n')

    COLUMNS = len(grid[0])
    ROWS = len(grid)

    def fewer_than_four_adjacent(x, y):
        adjacent_rolls = 0
        for dx, dy in filter(lambda it: it != (0,0), product((1, -1, 0), repeat=2)):
            column, row = x + dx, y + dy
            if 0 <= column < COLUMNS and 0 <= row < ROWS:
                adjacent_rolls += grid[row][column] == '@'
            if adjacent_rolls == 4:
                return False

        return True

    result = 0
    for i, row in enumerate(grid):
        for j, pos in enumerate(row):
            if pos == '.':
                continue
            if fewer_than_four_adjacent(j, i):
                result += 1

    return result
    