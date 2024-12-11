from enum import Enum
from copy import deepcopy


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def cw(self):
        return Dir((self.value + 1) % 4)

    def ccw(self):
        return Dir((self.value - 1) % 4)

    def move(self):
        return ((-1, 0), (0, 1), (1, 0), (0, -1))[self.value]

    def __str__(self):
        return ('^', '>', 'v', '<')[self.value]


class Pos(tuple):
    def __new__(cls, i, j, grid_size):
        return super(Pos, cls).__new__(cls, (i, j))

    def __init__(self, i, j, grid_size):
        self.grid_size = grid_size

    def __add__(self, d):
        di, dj = d.move()
        i = self[0] + di
        j = self[1] + dj
        if i in [-1, self.grid_size[0]] or j in [-1, self.grid_size[1]]:
            return None
        return Pos(i, j, self.grid_size)

    def next(self):
        if self[1] == self.grid_size[1] - 1:
            if self[0] == self.grid_size[0] - 1:
                return None
            else:
                return Pos(self[0] + 1, 0, self.grid_size)
        else:
            return Pos(self[0], self[1] + 1, self.grid_size)


class Trail:
    def __init__(self, pos):
        self.path = {k: set() for k in range(10)}
        self.path[0].add(pos)

    def find_path(self, next_z, pos):
        global z_map
        for d in [Dir.N, Dir.E, Dir.S, Dir.W]:
            next_pos = pos + d
            if next_pos and get_z(next_pos) == next_z:
                self.path[next_z].add(next_pos)

    # def print(self):
    #     global z_map
    #     grid = deepcopy(z_map)
    #     for lvl in self.path.keys():
    #         for pos in self.path[lvl]:
    #             grid[pos[0]][pos[1]] = f'\033[31m{lvl}\033[0m'
    #     print('-' * len(grid[0]))
    #     print(''.join([''.join([c for c in l]) + '\n' for l in grid])[:-1])
    #     print(f'score: {self.score()}')


    def score(self):
        return len(self.path[9])


def get_z(pos):
    global z_map
    try:
        return int(z_map[pos[0]][pos[1]])
    except ValueError:
        return -1


def main(data):
    grid_size = (len(data), len(data[0]))
    global z_map
    z_map = [[c for c in l] for l in data]

    trails = []
    cursor = Pos(0, 0, grid_size)
    while cursor is not None:
        if get_z(cursor) == 0:
            trail = Trail(cursor)
            for lvl in trail.path.keys():
                for pos in trail.path[lvl]:
                    trail.find_path(lvl + 1, pos)
            # trail.print()
            trails.append(trail)
        cursor = cursor.next()

    return sum([t.score() for t in trails])


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example5.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
