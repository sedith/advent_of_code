import numpy as np
import time


def scratch_card(card):
    nums_win, nums_you = card.split(': ')[1].split(' | ')
    nums_win = [s for s in nums_win.split(' ') if s != '']  # s != '' is there to account for double spaces
    nums_you = [s for s in nums_you[:-1].split(' ') if s != '']  # [:-1] to remove '\n'
    nb_win = 0
    for n in nums_you:
        nb_win += n in nums_win
    return 2**(nb_win-1) * bool(nb_win)  # x bool is there to nullify when nb_win == 0 (instead of having **-1)

if __name__ == '__main__':
    tic = time.time()

    with open('example.txt', 'r') as f:
        cards = f.readlines()

    total_points = 0
    for card in cards:
        total_points += scratch_card(card)

    total_points = int(total_points)

    toc = time.time()
    print('total of points:', total_points)
    print('time:', toc-tic)
