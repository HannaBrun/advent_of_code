from common import parse_file

def run():
    data = parse_file(5)
    range_rows, ids = data.split('\n\n')
    
    result = 0
    ranges = []
    for row in sorted(range_rows.split('\n'), key=lambda el: tuple(map(int, el.split('-')))):
        start, stop = map(int, row.split('-'))
        r = range(start, stop+1)
        ranges.append(r)

    for idx in ids.split('\n'):
        int_idx = int(idx)
        for range_ in ranges:
            if int_idx in range_:
                result += 1
                break

    return result
