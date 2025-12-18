from math import prod
from itertools import groupby


def main_legible(data):
    return sum(prod(op[:-1]) if op[-1] == '*' else sum(op[:-1]) for op in [tuple(int(''.join(ss).strip()) for ss in s[:-1]) + (int(''.join(s[-1][:-1]).strip()), s[-1][-1]) for s in [list(g) for k, g in groupby(zip(*[l[::-1] for l in data]), key=lambda r: all(c == ' ' for c in r)) if not k]])


def main(data):
    ops = []
    grand_total = 0
    for number, op in map(lambda t: (''.join(t[:-1]), t[-1]), zip(*[l[::-1] for l in data])):
        if n := number.split():
            ops.append(int(n[0]))
            if op != ' ':
                grand_total += prod(map(int, ops)) if op == '*' else sum(map(int, ops))
                ops = []
    return grand_total


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
