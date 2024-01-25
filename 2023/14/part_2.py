import numpy as np
import time
from copy import deepcopy


EMPTY = '.'
ROCK = 'O'
WALL = '#'


class Platform:
    def __init__(self, platform):
        self._grid = np.array([list(line) for line in platform])
        self.shape = self._grid.shape


    def __str__(self):
        return ''.join([''.join(line)+'\n' for line in self._grid])


    def __getitem__(self, index):
        return self._grid[tuple(index)]


    def __setitem__(self, index, val):
        self._grid[tuple(index)] = val


    def __eq__(self, val):
        return (self._grid == val._grid).all()


    def tilt(self, dir):
        if dir == 'N':
            for j in range(self.shape[1]):
                free = 0
                for i in range(self.shape[0]):
                    if self[i,j] == EMPTY:
                        free += 1
                    elif self[i,j] == WALL:
                        free = 0
                    elif free > 0:  # cell is ROCK and there is free room above
                        self[i,j] = EMPTY
                        self[i - free,j] = ROCK
        elif dir == 'S':
            for j in range(self.shape[1]):
                free = 0
                for i in range(self.shape[0])[::-1]:
                    if self[i,j] == EMPTY:
                        free += 1
                    elif self[i,j] == WALL:
                        free = 0
                    elif free > 0:
                        self[i,j] = EMPTY
                        self[i + free,j] = ROCK
        elif dir == 'W':
            for i in range(self.shape[0]):
                free = 0
                for j in range(self.shape[1]):
                    if self[i,j] == EMPTY:
                        free += 1
                    elif self[i,j] == WALL:
                        free = 0
                    elif free > 0:
                        self[i,j] = EMPTY
                        self[i,j-free] = ROCK
        if dir == 'E':
            for i in range(self.shape[0]):
                free = 0
                for j in range(self.shape[1])[::-1]:
                    if self[i,j] == EMPTY:
                        free += 1
                    elif self[i,j] == WALL:
                        free = 0
                    elif free > 0:
                        self[i,j] = EMPTY
                        self[i,j + free] = ROCK


    def get_load_north(self):
        load = 0
        for i,row in enumerate(self._grid):
            load += (self.shape[0] - i) * list(row).count(ROCK)
        return load


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    platform = Platform(input)
    nb_cycles = 1000000000
    memory = []
    for i in range(nb_cycles):
        h = hash(platform._grid.tobytes())
        memory.append(deepcopy(platform))
        for dir in ['N', 'W', 'S', 'E']:
            platform.tilt(dir)
        if platform in memory:
            loop_end = i
            loop_begin = memory.index(platform)
            break

    idx_end = ((nb_cycles-loop_begin) % (loop_end+1 - loop_begin)) + loop_begin
    platform = memory[idx_end]
    total_load = platform.get_load_north()

    toc = time.time()
    print('total load:', total_load)
    print('time:', toc-tic)
