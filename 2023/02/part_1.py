import time


BAG = {'red': 12, 'green': 13, 'blue': 14}

if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        games = f.read().splitlines()

    sum_IDs = 0
    for game in games:
        game_ID, game_content = game.split(': ')
        game_ID = int(game_ID[5:])
        sets = game_content.split('; ')
        valid = True
        for set in sets:
            subsets = set.split(', ')
            for subset in subsets:
                nb, color = subset.split(' ')
                if int(nb) > BAG[color]:
                    print(game_ID, ':', nb, color)
                    valid = False
                    break
        if valid:
            sum_IDs += game_ID

    toc = time.time()
    print('sum of IDs:', sum_IDs)
    print('time:', toc-tic)
