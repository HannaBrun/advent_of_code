def get_amount(color: str):
    try:
        result = next(filter(lambda it: color in it, colors))
        amount = int(result.split(' ')[0])
    except StopIteration:
        amount = 0

    return amount

game_sum = 0

with open('games.txt') as file:
    for line in file.readlines():
        idx, setups = line.split(': ')
        idx = int(idx.split(' ')[-1])
        setups = setups.split('; ')

        green = 0
        blue = 0
        red = 0
        for setup in setups:
            colors = setup.split(', ')
            green = max(get_amount('green'), green)
            blue = max(get_amount('blue'), blue)
            red = max(get_amount('red'), red)

        game_sum += (green * blue * red)

print(game_sum)
