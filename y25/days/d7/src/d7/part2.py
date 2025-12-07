from functools import cache
from common import parse_file


def count_timelines(rows, beam):
    @cache
    def trace_path(row_id, beam):
        if row_id == len(rows):
            return 1

        splitters = [i for i, ch in enumerate(rows[row_id]) if ch == '^']
        if beam in splitters:
            return trace_path(row_id+1, beam-1) + trace_path(row_id+1, beam+1)
        
        return trace_path(row_id+1, beam)
        
    return trace_path(0, beam)


def run():
    data = parse_file(7).splitlines()
    beam = data.pop(0).index('S')

    result = count_timelines(data, beam)
    return result
