from functools import reduce
import operator
from common import parse_file


def run():
    data = parse_file(6)
    problems = map(list, zip(*map(
        lambda el: list(filter(lambda it: it, el.split(' '))),
        data.split('\n')
    )))

    def func(op: str): return operator.add if op == '+' else operator.mul

    result = 0
    for problem in problems:
        result += reduce(func(problem[-1]), map(int, problem[:-1])) 

    return result
