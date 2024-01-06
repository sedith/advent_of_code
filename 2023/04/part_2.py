import numpy as np
import time


def scratch_card(card):
    nb_win = 0
    for n in card[1]:
        nb_win += n in card[0]
    return nb_win


def parse_cards(cards_txt):
    cards = {}
    for card in cards_txt:
        card_header, card_nums = card.split(': ')
        card_id = int(card_header.split()[1])
        nums_win, nums_you = card_nums.split(' | ')
        nums_win = [int(s) for s in nums_win.split()]
        nums_you = [int(s) for s in nums_you[:-1].split()]  # [:-1] to remove '\n'
        cards[card_id] = [nums_win, nums_you, 1]  # (winning cards, your cards, nb of copies)
    return cards


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        cards = parse_cards(f.readlines())

    nb_cards = 0
    for id in cards.keys():
        nb_cards += cards[id][-1]
        nb_win = scratch_card(cards[id])
        for _ in range(cards[id][-1]):
            for j in range(nb_win):
                cards[id+1+j][-1] += 1

    toc = time.time()
    print('total of points:', nb_cards)
    print('time:', toc-tic)
