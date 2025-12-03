from common import parse_file

def run():
    data = parse_file('d3')

    result = 0
    for row in data.split('\n'):
        cells = list(row)
        biggest_cell = max(cells[:-1])
        biggest_cell_idx = cells.index(biggest_cell)
        second_biggest_cell = max(cells[biggest_cell_idx+1:])
        
        result += int(''.join((biggest_cell, second_biggest_cell)))

    return result
