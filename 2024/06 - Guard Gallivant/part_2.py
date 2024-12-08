import time
from enum import Enum
from copy import deepcopy
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


class Grid:
    def __init__(self, data):
        self.grid = [[c for c in l] for l in data]
        self.size = (len(data), len(data[0]))
        self.obs = []
        self.path = []
        self.nodes = defaultdict(list)

    def get(self, pos):
        return self.grid[pos[0]][pos[1]]

    def explore_cw_branch(self, pos_init, dir_init):
        branch_nodes = defaultdict(list)
        obs_pos = pos_init + dir_init
        dir = dir_init.cw()
        pos = pos_init
        while pos is not None:
            next_pos = pos + dir
            if next_pos is not None:
                if next_pos == obs_pos or self.get(next_pos) == '#':
                    branch_nodes[pos].append(dir)
                    dir = dir.cw()
                    # print(self.display(pos_init, dir_init, branch_nodes, obs_pos))
                    # input()
                    continue
                if (next_pos in self.nodes and dir in self.nodes[next_pos]) or (next_pos in branch_nodes and dir in branch_nodes[next_pos]):
                    self.obs.append(obs_pos)
                    break
            pos = next_pos

    # def display(self, pos, dir, path, obstruct):
    #     def get_char(pos, path):
    #         if len(path[pos]) == 1:
    #             return '|' if path[pos][0] in [Dir.N, Dir.S] else '-'
    #         elif len(path[pos]) == 2:
    #             return '|' if path[pos][0].value % 2 == path[pos][1].value % 2 else '+'
    #         else:
    #             return '+'
    #
    #     grid = deepcopy(self.grid)
    #     for pos_path in self.path:
    #         grid[pos_path[0]][pos_path[1]] = '\033[32mx\033[0m'  # actual path in green
    #     for pos_path in self.nodes:
    #         grid[pos_path[0]][pos_path[1]] = f'\033[32m{get_char(pos_path, self.nodes)}\033[0m'  # actual path in green
    #     for pos_path in path:
    #         grid[pos_path[0]][pos_path[1]] = f'\033[93m{get_char(pos_path, path)}\033[0m'  # hypothetical path in yellow
    #     grid[pos[0]][pos[1]] = f'\033[31m{dir}\033[0m'  # current guard position in red
    #     grid[obstruct[0]][obstruct[1]] = '\033[31mO\033[0m'  # proposed obstruction in red
    #     return ''.join(''.join(line) + '\n' for line in grid)[:-1]


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
            grid.path.append(guard_pos)
            if grid.get(next_pos) == '#':
                grid.nodes[guard_pos].append(dir)
                dir = dir.cw()
                continue
            elif next_pos not in grid.obs and next_pos not in grid.path:  # check if we can obstruct the next cell
                grid.explore_cw_branch(guard_pos, dir)
        guard_pos = next_pos

    toc = time.time()
    print('nb obstructions:', len(grid.obs))
    print('time:', toc - tic)
