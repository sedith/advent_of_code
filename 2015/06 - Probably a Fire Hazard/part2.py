import numpy as np


def main(data):
    grid = np.zeros((1000,1000), dtype=int)

    for line in data:
        *_, (x1, y1), _, (x2, y2) = (map(int, t.split(',')) for t in line.split())
        if line.startswith('turn on'):
            grid[x1:x2+1, y1:y2+1] += 1
        elif line.startswith('turn off'):
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid < 0] = 0
        else:
            grid[x1:x2+1, y1:y2+1] += 2
    return np.sum(grid)


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
