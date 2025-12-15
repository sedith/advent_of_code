def main(data):
    nb_bat = 12
    joltage = 0
    for bank in data:
        bat = ''
        cursor = 0
        for i in range(nb_bat):
            if i == nb_bat - 1:
                sub_bank = bank[cursor:]
            else:
                sub_bank = bank[cursor:-(nb_bat-1-i)]
            bat += max(sub_bank)
            cursor += sub_bank.index(bat[-1]) + 1
        joltage += int(bat)
    return joltage


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
