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
            if char != '.' and not char.isnumeric():
                self.symbols.append(i)

                for idx in range(i-1, i+2, 2):
                    option = self.numbers.get(idx, Number('0'))
                    option.active = True

    def active_numbers(self):
        nbrs = []
        for nbr in self.numbers.values():
            if nbr.active and not nbr.used:
                nbr.used = True
                nbrs.append(nbr.value)

        return nbrs

    def activate_with_ext_symbols(self, symbols):
        for i in symbols:
            for idx in range(i-1, i+2):
                option = self.numbers.get(idx, Number('0'))
                option.active = True

        return True

    def __repr__(self):
        string = ''
        for key, value in self.numbers.items():
            string += f'{key}: {value}, '

        return string[:-2]


with open('schematic.txt', 'r') as file:
    numbers_to_sum = []
    previous = None
    for i, line in enumerate(file.readlines()):
        this_line = Line(line, i)
        if previous is not None:
            # first check if symbols on this line is adjacent to any numbers on previous line.
            symbols_this_line = this_line.symbols
            previous.activate_with_ext_symbols(symbols_this_line)
            numbers_to_sum.extend(previous.active_numbers())

            # last check if symbols on previous line is adjacent to any numbers on this line.
            # Symbols on this line has already been checked against numbers on this line.
            symbols_previous = previous.symbols
            this_line.activate_with_ext_symbols(symbols_previous)

        numbers_to_sum.extend(this_line.active_numbers())

        previous = this_line

    print(sum(numbers_to_sum))
