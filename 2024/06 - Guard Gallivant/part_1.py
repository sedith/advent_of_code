import time
from enum import Enum


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def next(self):
        return Dir((self.value + 1) % 4)


class Idx(tuple):
    def __new__(cls, i, j, grid_size):
        return super(Idx, cls).__new__(cls, (i, j))

    def __init__(self, i, j, grid_size):
        self.grid_size = grid_size

    def __add__(self, d):
        i, j = self
        if d == Dir.W:
            j -= 1
        elif d == Dir.E:
            j += 1
        if d == Dir.N:
            i -= 1
        elif d == Dir.S:
            i += 1
        if i in [-1, self.grid_size[0]] or j in [-1, self.grid_size[1]]:
            return None
        return Idx(i, j, self.grid_size)


class Grid:
    def __init__(self, data):
        self.grid = [[c for c in l] for l in data]
        self.size = (len(data), len(data[0]))
        self.nb_X = 0
        self.marker_X = '\033[31mX\033[0m'

    def get(self, idx):
        return self.grid[idx[0]][idx[1]]

    def mark(self, idx):
        if self.get(idx) != self.marker_X:
            self.nb_X += 1
            self.grid[idx[0]][idx[1]] = self.marker_X

    def __str__(self):
        return ''.join(''.join(line) + '\n' for line in self.grid)[:-1]


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        grid = Grid(data)

    ## find start
    for i, l in enumerate(data):
        try:
            j = l.index('^')
            break
        except ValueError:
            pass

    dir = Dir(0)
    guard = Idx(i, j, grid.size)

    ## increment guard path
    while guard is not None:
        grid.mark(guard)
        while (next_idx := guard + dir) is not None and grid.get(next_idx) == '#':
            dir = dir.next()
        guard = next_idx

    toc = time.time()
    print('nb distinct positions:', grid.nb_X)
    print('time:', toc - tic)
