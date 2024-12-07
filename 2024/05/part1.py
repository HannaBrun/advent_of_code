import weakref


class Number:
    _refs = []

    def __new__(cls, value: str, after: str | None = None):
        try:
            instance = next(filter(lambda it: it().value == int(value), cls._refs))()
            instance.try_append(after)

            return instance
        except StopIteration:
            return super().__new__(cls)

    def __init__(self, value: str, after: str | None = None):
        ref = weakref.ref(self)
        if ref not in self._refs:
            self._refs.append(ref)
            self.value = int(value)

            self.is_before = []
            self.try_append(after)
            
    def __repr__(self):
        return f'Number: {self.value}'

    def try_append(self, after: str | None):
        size_before = len(self.is_before)
        if after is not None:
            try:
                after_instance = next(filter(lambda it: it().value == int(after), self._refs))()
            except StopIteration:
                after_instance = Number(after)

            if after_instance not in self.is_before:
                self.is_before.append(after_instance)

        return len(self.is_before) > size_before

    def __eq__(self, other) -> bool:
        return self is other

    def __lt__(self, other, first=None) -> bool:
        return other not in self.is_before


def main():
    with open('2024/05/input.txt', 'r') as fp:
        rules, updates = fp.read().split('\n\n')

    nbrs = []
    for rule in rules.split():
        nbr = Number(*rule.split('|'))
        if nbr not in nbrs:
            nbrs.append(nbr)

    page_sum = 0

    for update in updates.split():
        numbers = list(map(lambda el: Number(el), update.split(',')))
        correct = sorted(numbers, reverse=True)
        if numbers == correct:
            middle = len(numbers) // 2 + len(numbers) % 2 - 1
            page_sum += numbers[middle].value

    return page_sum


if __name__ == '__main__':
    page_sum = main()
    print(page_sum)
