from collections import Counter
from enum import Enum

class HandRank(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

class Hand:
    CARD_VALUES = {
        'A': 14,
        'K': 13,
        'Q' : 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    def __init__(self, line: list):
        cards_and_bid = line.strip('\n').split()
        self.cards = cards_and_bid[0]
        self.bid = int(cards_and_bid[1])

        self._determine_rank()

    def _determine_rank(self):
        card_count = Counter(self.cards).most_common()
        if len(card_count) == 1:
            self.rank = HandRank.FIVE_OF_A_KIND
        elif card_count[0][1] == 4:
            self.rank = HandRank.FOUR_OF_A_KIND
        elif card_count[0][1] == 3 and card_count[1][1] == 2:
            self.rank = HandRank.FULL_HOUSE
        elif card_count[0][1] == 3:
            self.rank = HandRank.THREE_OF_A_KIND
        elif card_count[0][1] == 2 and card_count[1][1] == 2:
            self.rank = HandRank.TWO_PAIRS
        elif card_count[0][1] == 2:
            self.rank = HandRank.ONE_PAIR
        else:
            self.rank = HandRank.HIGH_CARD

    def __gt__(self, other):
        if self.rank.value == other.rank.value:
            # compare highest card, left to right
            for i in range(5):
                if self.cards[i] == other.cards[i]:
                    if i == 4:
                        raise Exception
                    continue

                return Hand.CARD_VALUES[self.cards[i]] > Hand.CARD_VALUES[other.cards[i]]

        return self.rank.value > other.rank.value

    def __repr__(self):
        return self.cards


with open('hands.txt', 'r') as file:
    hands = []
    for line in file.readlines():
        hands.append(Hand(line))

    sorted_hands = sorted(hands)
    winnings = 0
    for rank, hand in enumerate(sorted_hands, 1):
        winnings += rank * hand.bid

    print(winnings)
