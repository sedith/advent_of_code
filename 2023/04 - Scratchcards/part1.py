def scratch_card(card):
    nums_win, nums_you = card.split(': ')[1].split(' | ')
    nums_win = [s for s in nums_win.split()]
    nums_you = [s for s in nums_you.split()]
    nb_win = 0
    for n in nums_you:
        nb_win += n in nums_win
    return 2 ** (nb_win - 1) * bool(nb_win)  # x bool is there to nullify when nb_win == 0 (instead of having **-1)


def main(data):
    total_points = 0
    for card in data:
        total_points += scratch_card(card)

    return int(total_points)


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
