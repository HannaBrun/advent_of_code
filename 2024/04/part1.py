import re


def main():
    with open('2024/04/input.txt', 'r') as fp:
        data = [line.strip() for line in fp.readlines()]

    xmas = 'XMAS'
    samx = 'SAMX'
    count = 0
    width = len(data[0])
    height = len(data)

    for i, row in enumerate(data):
        count += len(re.findall(xmas, row))
        count += len(re.findall(samx, row))

        topleft_to_bottomright_diagonal = []
        x, y = 0, i
        while x < width and x >= 0 and y < height:
            topleft_to_bottomright_diagonal.append(data[y][x])
            x += 1
            y += 1

        count += len(re.findall(xmas, ''.join(topleft_to_bottomright_diagonal)))
        count += len(re.findall(samx, ''.join(topleft_to_bottomright_diagonal)))

        bottomleft_to_topright_diagonal = []
        x, y = width - 1, i
        while x < width and x > 0 and y < height:
            bottomleft_to_topright_diagonal.append(data[y][x])
            x -= 1
            y += 1

        count += len(re.findall(xmas, ''.join(bottomleft_to_topright_diagonal)))
        count += len(re.findall(samx, ''.join(bottomleft_to_topright_diagonal)))


    for i, column in enumerate(zip(*data)):
        count += len(re.findall(xmas, ''.join(column)))
        count += len(re.findall(samx, ''.join(column)))

        topleft_to_bottomright_diagonal = []
        x, y = i, 0
        while x < width and x > 0 and y < height:
            topleft_to_bottomright_diagonal.append(data[y][x])
            x += 1
            y += 1

        count += len(re.findall(xmas, ''.join(topleft_to_bottomright_diagonal)))
        count += len(re.findall(samx, ''.join(topleft_to_bottomright_diagonal)))

        bottomleft_to_topright_diagonal = []
        x, y = width - i - 2, 0
        while x < width and x >= 0 and y < height:
            bottomleft_to_topright_diagonal.append(data[y][x])
            x -= 1
            y += 1

        count += len(re.findall(xmas, ''.join(bottomleft_to_topright_diagonal)))
        count += len(re.findall(samx, ''.join(bottomleft_to_topright_diagonal)))

    return count


if __name__ == '__main__':
    count = main()
    print(count)
