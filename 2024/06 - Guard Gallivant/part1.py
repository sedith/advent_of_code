from collections import defaultdict


def main(data):
    size = len(data), len(data[0])
    in_grid = lambda p: 0 <= p.imag < size[0] and 0 <= p.real < size[1]
    obs = {j + i * 1j for i, l in enumerate(data) for j, c in enumerate(l) if c == '#'}

    (p,) = (j + i * 1j for i, l in enumerate(data) for j, c in enumerate(l) if c == '^')  # find start
    dir = -1j  # starts facing north

    ## increment guard path
    path = set()
    while in_grid(p):
        path.add(p)
        while (np := p + dir) in obs:
            dir *= 1j  # rotate 90 degrees clockwise
        p = np
    return len(path)


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
