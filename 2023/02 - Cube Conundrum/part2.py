def main(data):
    sum_powers = 0
    for game in data:
        game_ID, game_content = game.split(': ')
        game_ID = int(game_ID[5:])
        sets = game_content.split('; ')
        mins = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets:
            subsets = set.split(', ')
            for subset in subsets:
                nb, color = subset.split(' ')
                mins[color] = max(mins[color], int(nb))
        sum_powers += mins['red'] * mins['green'] * mins['blue']

    return sum_powers


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
