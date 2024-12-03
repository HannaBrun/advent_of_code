import re


def main():
    with open('2024/03/input.txt', 'r') as fp:
        data = fp.read()

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    result = 0
    enabled = True
    for hit in re.finditer(pattern, data):
        match hit.group():
            case 'do()':
                enabled = True
            case 'don\'t()':
                enabled = False
            case _:
                x, y = hit.groups()
                result += int(x) * int(y) * enabled

    return result


if __name__ == '__main__':
    result = main()
    print(result)
