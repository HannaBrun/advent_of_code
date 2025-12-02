from common import parse_file


def has_repeating_pattern(number: str):
    if len(number) % 2:
        return False
    
    return number[:len(number) // 2] == number[len(number) // 2:]


def run():
    data = parse_file('d2')
    result = 0
    for span in data.split(','):
        lower, upper = span.split('-')
        for nbr in range(int(lower), int(upper)+1):
            if has_repeating_pattern(str(nbr)):
                result += nbr

    return result
