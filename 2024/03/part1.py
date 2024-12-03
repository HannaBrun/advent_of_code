import re


def main():
    with open('2024/03/input.txt', 'r') as fp:
        data = fp.read()

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    result = 0
    for mul in re.finditer(pattern, data):
        x, y = mul.groups()
        result += int(x) * int(y)

    return result


if __name__ == '__main__':
    result = main()
    print(result)
