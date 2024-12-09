from enum import Enum


class Dir(Enum):
    NE = 0
    SE = 1
    SW = 2
    NW = 3


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


    def has_4_neighbors(self):
        return not (self[0] in [0, self.grid_size[0] - 1] or self[1] in [0, self.grid_size[1] - 1])


    def __add__(self, d):
        i, j = self
        if d in [Dir.SW, Dir.NW]:
            j -= 1
        elif d in [Dir.SE, Dir.NE]:
            j += 1
        if d in [Dir.NW, Dir.NE]:
            i -= 1
        elif d in [Dir.SW, Dir.SE]:
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

    target_str = 'MAS'
    target_center = target_str[1]
    target_sides = ['M', 'S']

    counter = 0
    cursor = Idx(0, 0, grid.size)
    while cursor is not None:
        if grid.get(cursor) == target_center and cursor.has_4_neighbors() \
        and (nw := grid.get(cursor + Dir.NW)) in target_sides \
        and (se := grid.get(cursor + Dir.SE)) in target_sides and se != nw \
        and (sw := grid.get(cursor + Dir.SW)) in target_sides \
        and (ne := grid.get(cursor + Dir.NE)) in target_sides and sw != ne:
            counter += 1
            grid.reveal(cursor)
            [grid.reveal(cursor + Dir(d)) for d in range(4)]
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
