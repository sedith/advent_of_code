import numpy as np


EMPTY = '.'
ROCK = 'O'
WALL = '#'


class Platform:
    def __init__(self, platform):
        self._grid = np.array([list(line) for line in platform])
        self.shape = self._grid.shape

    def __str__(self):
        return ''.join([''.join(line) + '\n' for line in self._grid])

    def __getitem__(self, index):
        return self._grid[tuple(index)]

    def __setitem__(self, index, val):
        self._grid[tuple(index)] = val

    def tilt_north(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self[i, j] == ROCK:
                    k = i - 1
                    while k >= 0 and self[k, j] == EMPTY:
                        self[k, j] = ROCK
                        self[k + 1, j] = EMPTY
                        k -= 1

    def get_load(self):
        load = 0
        for i in range(self.shape[0]):
            row_load = self.shape[0] - i
            for cell in self[i, :]:
                if cell == ROCK:
                    load += row_load
        return load


def main(data):
    platform = Platform(data)
    platform.tilt_north()
    return platform.get_load()


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
