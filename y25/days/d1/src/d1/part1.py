from common import parse_file

class DialValue:
    def __init__(self):
        self.val = 50

    def __iadd__(self, other):
        nbr = int(other[1:])
        match other[0]:
            case 'R':
                sum_ = self.val + nbr
            case 'L':
                sum_ = self.val - nbr

        self.val = sum_ % 100
        return self

def run():
    data = parse_file('d1')

    value = DialValue()
    result = 0
    for row in data.split('\n'):
        value += row
        if not value.val:
            result += 1

    return result
