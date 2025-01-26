from collections import defaultdict
from functools import cache


def expand_stone(stone):
    if not stone:
        return [1]
    elif len(str_stone := str(stone)) % 2 == 0:
        n = len(str_stone) // 2
        return [int(str_stone[:n]), int(str_stone[n:])]
    else:
        return [stone * 2024]

@cache
def expand_rec(depth, stone):
    if not depth:
        return 1
    return sum(expand_rec(depth - 1, s) for s in expand_stone(stone))


def main(data):
    stones = list(map(int, data.split()))
    nb_iter = 25

    return sum([expand_rec(nb_iter, s) for s in stones])


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()[0]
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
