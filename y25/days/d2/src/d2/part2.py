from itertools import batched
from common import parse_file


def has_repeating_pattern(number: str):
    sum_ = 0
    for n in range(len(number) // 2, 0, -1):
        if len(number) % n:
            continue
        if len(set(batched(number, n))) == 1:
            sum_ += int(number[:n])
 
    return sum_


def run():
    data = parse_file('d2')
    result = 0
    for span in data.split(','):
        lower, upper = span.split('-')
        for nbr in range(int(lower), int(upper)+1):
            if has_repeating_pattern(str(nbr)):
                result += nbr

    return result
