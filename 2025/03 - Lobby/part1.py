def main(data):
    joltage = 0
    for bank in data:
        bat_1 = max(bank[:-1])
        idx = bank.index(bat_1)
        bat_2 = max(bank[idx+1:])
        joltage += int(bat_1 + bat_2)
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
