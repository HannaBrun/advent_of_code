from collections import Counter

def process_card():

    return 1

with open('scratchcards.txt', 'r') as file:
    nbr_of_cards = 0
    card_board = Counter()
    for i, line in enumerate(file.readlines(), 1):
        card_board[i] += 1
        card, row = line.replace('  ', ' ').split(':')
        win, nbrs = row.split('|')
        win = set(win.strip().split())
        nbrs = set(nbrs.strip().split())

        score = len(win & nbrs)
        for j in range(i+1, i+1+score):
            card_board[j] += card_board[i]

    list_of_cards = list(filter(lambda it: it <= i, card_board.elements()))

print(len(list_of_cards))
