import numpy as np
from scipy.signal import convolve2d


def main(data):
    grid = np.array([[p == '@' for p in line] for line in data], dtype=int)
    kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
    neighbours = convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=0)
    return np.sum((neighbours < 4) * (grid > 0))


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
