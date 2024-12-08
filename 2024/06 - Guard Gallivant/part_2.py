import time
from enum import Enum
from copy import copy, deepcopy
from collections import defaultdict


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def cw(self):
        return Dir((self.value + 1) % 4)

    def ccw(self):
        return Dir((self.value - 1) % 4)

    def __str__(self):
        return ('^', '>', 'v', '<')[self.value]


class Pos(tuple):
    def __new__(cls, i, j, grid_size):
        return super(Pos, cls).__new__(cls, (i, j))

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
        return Pos(i, j, self.grid_size)


class Grid:
    def __init__(self, data):
        self.grid = [[c for c in l] for l in data]
        self.size = (len(data), len(data[0]))
        self.obs = []
        self.path = defaultdict(list)

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def explore_cw_branch(self, pos_init, dir_init):
        branch_path = defaultdict(list)
        obs_pos = pos_init + dir_init
        dir = dir_init.cw()
        pos = pos_init
        while pos is not None:
            branch_path[pos].append(dir)
            next_pos = pos + dir
            if next_pos is not None:
                if next_pos == obs_pos or self.get(next_pos) == '#':
                    dir = dir.cw()
                    continue
                elif (next_pos in self.path.keys() and dir in self.path[next_pos]) \
                or (next_pos in branch_path.keys() and dir in branch_path[next_pos]):
                    self.obs.append(obs_pos)
                    break
            pos = next_pos

    def display(self, pos, dir, path, obstruct):
        def get_char(pos, path):
            if len(path[pos]) == 1:
                return '|' if path[pos][0] in [Dir.N, Dir.S] else '-'
            elif len(path[pos]) == 2:
                return '|' if path[pos][0].value % 2 == path[pos][1].value % 2 else '+'
            else:
                return '+'
        grid = deepcopy(self.grid)
        for pos_path in self.path.keys():
            grid[pos_path[0]][pos_path[1]] = f'\033[32m{get_char(pos_path, self.path)}\033[0m'  # actual path in green
        for pos_path in path.keys():
            grid[pos_path[0]][pos_path[1]] = f'\033[93m{get_char(pos_path, path)}\033[0m'  # hypothetical path in yellow
        grid[pos[0]][pos[1]] = f'\033[31m{dir}\033[0m'  # current guard position in red
        grid[obstruct[0]][obstruct[1]] = '\033[31mO\033[0m'  # proposed obstruction in red
        return ''.join(''.join(line) + '\n' for line in grid)[:-1]


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
    guard_pos = Pos(i, j, grid.size)

    ## increment guard path
    while guard_pos is not None:
        next_pos = guard_pos + dir
        if next_pos is not None:
            grid.path[guard_pos].append(dir)
            if grid.get(next_pos) == '#':
                dir = dir.cw()
                continue
            elif next_pos not in grid.obs and next_pos not in grid.path.keys():  # check if we can obstruct the next cell
                grid.explore_cw_branch(guard_pos, dir)
        guard_pos = next_pos

    toc = time.time()
    print('nb obstructions:', len(grid.obs))
    print('time:', toc - tic)
