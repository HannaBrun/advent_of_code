from collections import Counter
from enum import Enum

class HandRank(Enum):
    FIVE_OF_A_KIND = 5
    FOUR_OF_A_KIND = 4
    FULL_HOUSE = 3.5
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2.5
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __add__(self, adder):
        return HandRank(self.value + adder)


class Hand:
    CARD_VALUES = {
        'A': 14,
        'K': 13,
        'Q' : 12,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 0
    }

    def __init__(self, line: list):
        cards_and_bid = line.strip('\n').split()
        self.cards = cards_and_bid[0]
        self.bid = int(cards_and_bid[1])

        self._determine_rank()

    def _determine_rank(self):
        counter = Counter(self.cards)
        jokers = 0
        if 'J' in counter:
            jokers += counter.pop('J')

        card_count = counter.most_common()

        if len(card_count) <= 1:
            self.rank = HandRank.FIVE_OF_A_KIND
        elif card_count[0][1] == 4:
            self.rank = HandRank.FOUR_OF_A_KIND + jokers
        elif card_count[0][1] == 3 and card_count[1][1] == 2:
            self.rank = HandRank.FULL_HOUSE
        elif card_count[0][1] == 3:
            self.rank = HandRank.THREE_OF_A_KIND + jokers
        elif card_count[0][1] == 2 and card_count[1][1] == 2:
            self.rank = HandRank.TWO_PAIRS + jokers
        elif card_count[0][1] == 2:
            self.rank = HandRank.ONE_PAIR + jokers
        else:
            self.rank = HandRank.HIGH_CARD + jokers

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
