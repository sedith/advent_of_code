from math import prod


def main(data):
    ops = zip(*map(lambda l: l.split(), data))
    return sum(prod(map(int, op[:-1])) if op[-1] == '*' else sum(map(int, op[:-1])) for op in ops)

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
