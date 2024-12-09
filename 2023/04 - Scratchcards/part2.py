def scratch_card(card):
    nb_win = 0
    for n in card[1]:
        nb_win += n in card[0]
    return nb_win


def parse_cards(cards_text):
    cards = {}
    for card in cards_text:
        card_header, card_nums = card.split(': ')
        card_id = int(card_header.split()[1])
        nums_win, nums_you = card_nums.split(' | ')
        nums_win = [int(s) for s in nums_win.split()]
        nums_you = [int(s) for s in nums_you.split()]
        cards[card_id] = [nums_win, nums_you, 1]  # (winning cards, your cards, nb of copies)
    return cards


def main(data):
    cards = parse_cards(data)

    nb_cards = 0
    for id in cards.keys():
        nb_cards += cards[id][-1]
        nb_win = scratch_card(cards[id])
        for _ in range(cards[id][-1]):
            for j in range(nb_win):
                cards[id + 1 + j][-1] += 1

    return nb_cards


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
