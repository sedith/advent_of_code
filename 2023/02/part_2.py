import time


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        games = f.readlines()

    sum_powers = 0
    for game in games:
        game_ID, game_content = game.split(': ')
        game_ID = int(game_ID[5:])
        sets = game_content[:-1].split('; ')
        mins = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets:
            subsets = set.split(', ')
            for subset in subsets:
                nb, color = subset.split(' ')
                mins[color] = max(mins[color], int(nb))
        sum_powers += mins['red'] * mins['green'] * mins['blue']

    toc = time.time()
    print('sum of powers:', sum_powers)
    print('time:', toc-tic)
