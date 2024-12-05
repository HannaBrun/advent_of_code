
def main():
    with open('2024/04/input.txt', 'r') as fp:
        data = [line.strip() for line in fp.readlines()]

    count = 0
    width = len(data[0])
    height = len(data)
    ms_sm = ('MS', 'SM')

    for i, row in enumerate(data):
        if i in (0, height-1):
            continue

        for j, letter in enumerate(row):
            if letter != 'A' or j in (0, width-1):
                continue
            topleft_to_bottomright_diagonal = data[i-1][j-1] + data[i+1][j+1]
            bottomleft_to_topright_diagonal = data[i+1][j-1] + data[i-1][j+1]

            if topleft_to_bottomright_diagonal in ms_sm and bottomleft_to_topright_diagonal in ms_sm:
                count += 1

    return count


if __name__ == '__main__':
    count = main()
    print(count)
