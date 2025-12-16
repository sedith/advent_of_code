import numpy as np
from scipy.signal import convolve2d


def main(data):
    grid = np.array([[p == '@' for p in line] for line in data], dtype=int)
    kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])

    def remove_rolls(grid):
        neighbours = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
        removables = (neighbours < 4) * (grid > 0)
        return np.sum(removables), np.invert(removables) * grid

    total_removed = 0
    nb_removal = 1
    while nb_removal > 0:
        nb_removal, grid = remove_rolls(grid)
        total_removed += nb_removal
    return total_removed


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
