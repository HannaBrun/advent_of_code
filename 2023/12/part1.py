import itertools
import time

def parse(possibility: list):
    return [
        str(len(springs_in_a_row))
        for spring_group in possibility
        for springs_in_a_row in filter(lambda it: it, spring_group.split('0'))
    ]


with open('condition.txt', 'r') as file:
    count = 0
    start = time.perf_counter()
    for line in file.read().splitlines():
        springs, _, schema = line.partition(' ')
        schema = schema.split(',')

        spring_groups = filter(lambda it: it, springs.split('.'))
        list_of_combos = []
        for group in spring_groups:
            unknowns = len(group.replace('#', ''))
            unknown_combos = 2 ** unknowns

            combos = [bin(combo)[2:].zfill(unknowns) for combo in range(unknown_combos)]
            for i, char in enumerate(group):
                if char == '#':
                    combos = list(map(lambda el: el[:i] + '1' + el[i:], combos))

            list_of_combos.append(combos)

        possibilities = itertools.product(*list_of_combos)
        for possibility in possibilities:
            if parse(possibility) == schema:
                count += 1

    print(count)
    print(f'{time.perf_counter() - start:.2f}')
    # 7916


