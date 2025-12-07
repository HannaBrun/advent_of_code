from functools import reduce
import operator
from common import parse_file


def run():
    data = parse_file(6).split('\n')
    def func(op: str):
        if op == ' ':
            return False
        return operator.add if op == '+' else operator.mul

    operator_row = data[-1]
    nbr_rows = list(map(list, data[:-1]))
    result = 0
    current_op = None
    for op in filter(lambda it: it, operator_row.split(' ')):
        op_or_blank = func(op)
        if op_or_blank:
            current_op = op_or_blank
        
        nbrs_to_operate = []
        while True:
            nbr_str = ''
            for row in nbr_rows:
                try:
                    nbr_or_blank = row.pop(0)
                except IndexError:
                    continue
                if nbr_or_blank != ' ':
                    nbr_str += nbr_or_blank
            if not nbr_str:
                break
            nbrs_to_operate.append(int(nbr_str))
        
        result += reduce(current_op, nbrs_to_operate)
            
    return result
