from math import log


def concat(a, b):
    return a * (10 ** int(log(b, 10) + 1)) + b


def _rec_check(result, possibilies, numbers):
    if not numbers:
        return possibilies
    else:
        new_pos = []
        for p in possibilies:
            sum = p + numbers[0]
            mul = p * numbers[0]
            conc = concat(p, numbers[0])
            if result >= sum:
                new_pos.append(sum)
            if result >= mul:
                new_pos.append(mul)
            if result >= conc:
                new_pos.append(conc)

    return _rec_check(result, new_pos, numbers[1:])


def main(data):
    sum_calib = 0
    for equation in data:
        result, numbers = equation.split(':')
        result = int(result)
        numbers = list(map(int, numbers.split()))

        sum_calib += result * (result in _rec_check(result, [numbers[0]], numbers[1:]))

    return sum_calib


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
