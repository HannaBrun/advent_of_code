class Gear:
    def __init__(self, idx: int):
        self.idx = idx
        self.numbers = []

    def add_number(self, nbr: int):
        if nbr > 0:
            self.numbers.append(nbr)

    def add_numbers_adjacent_line(self, numbers):
        prev_nbr = Number('-1')
        for i in range(self.idx-1, self.idx+2):
            option = numbers.get(i, Number('0'))
            if option == prev_nbr:
                continue
            self.add_number(option.value)
            prev_nbr = option

    def is_true_gear(self) -> bool:
        return len(self.numbers) >= 2


class Number:
    def __init__(self, value: str):
        self.str_value = value
        self.value = int(value)
        self.size = len(value)

        self.active = False
        self.used = False

    def __repr__(self):
        return self.str_value


class Line:
    def __init__(self, data: str, iter_i: int):
        data = data.strip('\n')
        self.numbers = {}

        nbrs = list(map(
            lambda el: Number(el),
            filter(
                lambda it: it,
                ''.join(map(
                    lambda el: el if el.isnumeric() else '.',
                    data
                )).split('.')
            )
        ))

        idx = -1
        for nbr in nbrs:
            idx = data.find(nbr.str_value, idx + 1)
            for i in range(idx, idx + nbr.size):
                self.numbers[i] = nbr

        self.symbols = []
        for i, char in enumerate(data):
            if char == '*':
                self.symbols.append(Gear(i))

                for idx in range(i-1, i+2, 2):
                    option = self.numbers.get(idx, Number('0'))
                    self.symbols[-1].add_number(option.value)

    def __repr__(self):
        string = ''
        for key, value in self.numbers.items():
            string += f'{key}: {value}, '

        return string[:-2]


def cumsum(array):
    res = 1
    for el in array:
        res *= el

    return res


with open('schematic.txt', 'r') as file:
    numbers_to_sum = []
    symbols = []
    previous_line = None
    for i, line in enumerate(file.readlines()):
        this_line = Line(line, i)
        symbols.extend(this_line.symbols)

        if previous_line is not None:
            symbols_this_line = this_line.symbols
            for symb in symbols_this_line:
                symb.add_numbers_adjacent_line(previous_line.numbers)

            symbols_previous = previous_line.symbols
            for symb in symbols_previous:
                symb.add_numbers_adjacent_line(this_line.numbers)

        previous_line = this_line

    symbols_summed = sum(map(
        lambda el: cumsum(el.numbers),
        filter(
            lambda it: it.is_true_gear(),
            symbols
        )
    ))

    print(symbols_summed)
