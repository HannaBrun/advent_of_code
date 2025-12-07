from common import parse_file


class AddableRanges(list):
    def __init__(self, *args):
        list.__init__(self, *args)    

    def add(self, range_string: str):
        start, stop = map(int, range_string.split('-'))
        new_range = range(start, stop+1)
        if not self:
            self.append(new_range)
            return

        last_range = self[-1]

        if stop in last_range:
            return
        if start in last_range and stop > last_range[-1]:
            self[-1] = range(last_range[0], stop+1)
            return

        self.append(new_range)


def run():
    data = parse_file(5)
    range_rows, _ = data.split('\n\n')
    
    ranges = AddableRanges()
    for row in sorted(range_rows.split('\n'), key=lambda el: tuple(map(int, el.split('-')))):
        ranges.add(row)

    result = sum(map(len, ranges))

    return result
