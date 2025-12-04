from common import parse_file

def run():
    data = parse_file(3)

    result = 0
    for row in data.split('\n'):
        cells = list(row)

        activated_cells = []
        biggest_cell_idx = -1
        for i in range(12, 0, -1):
            if i == 1:
                biggest_cell = max(cells[biggest_cell_idx+1:])
            else:
                biggest_cell = max(cells[biggest_cell_idx+1:-i+1])
            activated_cells.append(biggest_cell)

            biggest_cell_idx = cells.index(biggest_cell, biggest_cell_idx+1)
        
        result += int(''.join(activated_cells))

    return result
