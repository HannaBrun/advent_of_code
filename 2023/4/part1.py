with open('scratchcards.txt', 'r') as file:
    total_score = 0
    for line in file.readlines():
        card, row = line.replace('  ', ' ').split(':')
        win, nbrs = row.split('|')
        win = set(win.strip().split())
        nbrs = set(nbrs.strip().split())

        union = win & nbrs
        score = int(2 ** (len(union) - 1))
        total_score += score

print(total_score)