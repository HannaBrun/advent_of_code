from common import parse_file

class DialValue:
    def __init__(self):
        self.val = 50
        self.last_nbr_of_zeros = 0

    def __iadd__(self, other):
        nbr = int(other[1:])
        match other[0]:
            case 'R':
                sum_ = self.val + nbr
            case 'L':
                sum_ = self.val - nbr

        if not self.val and sum_ < 0:
            self.last_nbr_of_zeros = abs((sum_-1) // 100) - 1
        elif sum_ <= 0:
            self.last_nbr_of_zeros = abs((sum_-1) // 100)
        else:
            self.last_nbr_of_zeros = abs(sum_ // 100)
        
        self.val = sum_ % 100
        return self

def run():
    data = parse_file('d1')

    value = DialValue()
    result = 0
    for row in data.split('\n'):
        value += row
        result += value.last_nbr_of_zeros

    return result
