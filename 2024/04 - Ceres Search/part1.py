from enum import Enum


class Dir(Enum):
    N = 0
    NE = 1
    E = 2
    SE = 3
    S = 4
    SW = 5
    W = 6
    NW = 7


class Idx(tuple):
    def __new__(cls, i, j, grid_size):
        return super(Idx, cls).__new__(cls, (i, j))


    def __init__(self, i, j, grid_size):
        self.grid_size = grid_size


    def next(self):
        if self[1] == self.grid_size[1] - 1:
            if self[0] == self.grid_size[0] - 1:
                return None
            else:
                return Idx(self[0] + 1, 0, self.grid_size)
        else:
            return Idx(self[0], self[1] + 1, self.grid_size)


    def get_neighbors(self):
        if self[0] == 0:
            return [Dir.E, Dir.SE, Dir.S, Dir.SW, Dir.W]
        elif self[0] == self.grid_size[0] - 1:
            return [Dir.N, Dir.NE, Dir.E, Dir.W, Dir.NW]
        if self[1] == 0:
            return [Dir.N, Dir.NE, Dir.E, Dir.SE, Dir.S]
        elif self[1] == self.grid_size[1] - 1:
            return [Dir.N, Dir.S, Dir.SW, Dir.W, Dir.NW]
        return [Dir(k) for k in range(8)]


    def __add__(self, d):
        i, j = self
        if d in [Dir.SW, Dir.W, Dir.NW]:
            j -= 1
        elif d in [Dir.SE, Dir.E, Dir.NE]:
            j += 1
        if d in [Dir.NW, Dir.N, Dir.NE]:
            i -= 1
        elif d in [Dir.SW, Dir.S, Dir.SE]:
            i += 1
        if i in [-1, self.grid_size[0]] or j in [-1, self.grid_size[1]]:
            return None
        return Idx(i, j, self.grid_size)


class Grid:
    def __init__(self, input):
        self.grid = input
        self.size = (len(input), len(input[0]))
        self.str = [['.' for _ in l] for l in input]

    def get(self, idx):
        return self.grid[idx[0]][idx[1]]

    def reveal(self, idx):
        self.str[idx[0]][idx[1]] = self.get(idx)

    def __str__(self):
        return ''.join(''.join(line) + '\n' for line in self.str)[:-1]


def main(data):
    grid = Grid(data)
    target_str = 'XMAS'

    counter = 0
    cursor = Idx(0, 0, grid.size)
    while cursor is not None:
        if grid.get(cursor) == target_str[0]:
            for d in cursor.get_neighbors():
                disp_idx = [cursor]
                i = 1
                idx = cursor + d
                while idx is not None and grid.get(idx) == target_str[i]:
                    disp_idx.append(idx)
                    if i == len(target_str) - 1:
                        counter += 1
                        [grid.reveal(idx) for idx in disp_idx]
                        break
                    i += 1
                    idx += d
        cursor = cursor.next()

    return counter


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
