import numpy as np
import time


HEAD_VALUES = {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'}  # convert letter card to digit in hexa
TYPES = {'five': 6, 'four': 5, 'full': 4, 'three': 3, 'twopairs': 2, 'pair': 1, 'high': 0}


def card_val(card):
    if card.isdigit():
        return card
    else:
        return HEAD_VALUES[card]


def hand_to_id(hand):
    card_score = int(''.join(map(card_val, hand)), 16)

    type = TYPES['high']
    for i, card in enumerate(hand[:-1]):
        if card in hand[:i]: continue  # disregard cards that have been checked already
        count = hand.count(card)
        if count == 5:
            type = TYPES['five']
            break
        if count == 4:
            type = TYPES['four']
            break
        if count == 3:
            if type == TYPES['pair']:
                type = TYPES['full']
                break
            else:
                type = TYPES['three']
        if count == 2:
            if type == TYPES['three']:
                type = TYPES['full']
                break
            elif type == TYPES['pair']:
                type = TYPES['twopairs']
                break
            else:
                type = TYPES['pair']

    type_score = 1000000 * type
    return card_score + type_score


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        inputs = f.read().splitlines()

    hands, bids = zip(*[line.split() for line in inputs])
    ids = map(hand_to_id, hands)
    bids = map(int, bids)

    ids, hands, bids = zip(*sorted(zip(ids, hands, bids)))

    total = sum([(rank + 1)* bid for rank, bid in enumerate(bids)])

    toc = time.time()
    print('total winnings:', total)
    print('time:', toc-tic)
