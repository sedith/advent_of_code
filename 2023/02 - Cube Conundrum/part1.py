BAG = {'red': 12, 'green': 13, 'blue': 14}


def main(data):
    sum_IDs = 0
    for game in data:
        game_ID, game_content = game.split(': ')
        game_ID = int(game_ID[5:])
        sets = game_content.split('; ')
        valid = True
        for set in sets:
            subsets = set.split(', ')
            for subset in subsets:
                nb, color = subset.split(' ')
                if int(nb) > BAG[color]:
                    valid = False
                    break
        if valid:
            sum_IDs += game_ID

    return sum_IDs


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
