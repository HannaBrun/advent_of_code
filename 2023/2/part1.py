MAX_GREEN = 13
MAX_BLUE = 14
MAX_RED = 12


def get_amount(color: str):
    try:
        result = next(filter(lambda it: color in it, colors))
        amount = int(result.split(' ')[0])
    except StopIteration:
        amount = 0

    return amount


game_sum = 0

with open('games.txt') as file:
    for idx, line in enumerate(file.readlines(), 1):
        _, setups = line.split(': ')
        # idx = int(idx.split(' ')[-1])
        setups = setups.split('; ')

        for setup in setups:
            colors = setup.split(', ')
            green = get_amount('green')
            blue = get_amount('blue')
            red = get_amount('red')

            if green > MAX_GREEN or blue > MAX_BLUE or red > MAX_RED:
                break
        else:
            game_sum += idx

print(game_sum)
