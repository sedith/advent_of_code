import numpy as np
import time
from typing import NamedTuple


def add(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


def is_in_grid(cell, grid):
    return cell.ij[0] >= 0 and cell.ij[0] < grid.shape[0] and cell.ij[1] >= 0 and cell.ij[1] < grid.shape[1]


REFLECT_SLASH = {'U': 'R', 'L': 'D', 'D': 'L', 'R': 'U'}  # for / tiles
REFLECT_BACKSLASH = {'U': 'L', 'R': 'D', 'D': 'R', 'L': 'U'}  # for \ tiles
MOVES = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
class CellState(NamedTuple):
    ij: tuple[int,int] = (0,0)
    dir: str = 'R'

    def move(self, new_dir=None):
        dir = self.dir if new_dir is None else new_dir
        return CellState(add(self.ij, MOVES[dir]), dir)


def get_next_interesting_cell(cell, map):
    chain = []
    while is_in_grid(cell, map) and map[cell.ij] in ['.', '\\', '/']:
        chain.append(cell.ij)
        if map[cell.ij] == '.':
            cell = cell.move()
        elif map[cell.ij] == '\\':
            cell = cell.move(REFLECT_BACKSLASH[cell.dir])
        else:  # map[cell.ij] == '/':
            cell = cell.move(REFLECT_SLASH[cell.dir])

    if is_in_grid(cell, map):
        return cell, chain
    else:
        return None, chain


def propagate(start_cell, map, memoization):
    path = {start_cell: {'next': [], 'chain': []}}
    states = [start_cell]
    seen = []

    while states:
        curr = states.pop()

        if curr in memoization:
            path[curr] = memoization[curr]
            new_cells = path[curr]['next']
        else:
            if not curr == start_cell:
                path[curr]['chain'].append(curr.ij)
                cell = curr.move()
            else:
                cell = curr

            cell, chain = get_next_interesting_cell(cell, map)
            path[curr]['chain'] += chain

            if cell is None:  # the ray hits a wall
                new_cells = []
            else:  # the ray hits a splitter
                if map[cell.ij] == '-':
                    if cell.dir == 'L' or cell.dir == 'R':
                        new_cells = [cell]
                    else:
                        new_cells = [CellState(cell.ij, 'L'), CellState(cell.ij, 'R')]
                else:  # map[cell.ij] == '|':
                    if cell.dir == 'U' or cell.dir == 'D':
                        new_cells = [cell]
                    else:
                        new_cells = [CellState(cell.ij, 'U'), CellState(cell.ij, 'D')]
                path[curr]['next'] = new_cells

        seen += path[curr]['chain']
        new_cells = [nc for nc in new_cells if nc not in path]

        for nc in new_cells:
            path[nc] = {'next': [], 'chain': []}
        states += new_cells

    memoization.update(path)
    return len(set(seen))


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        contraption = f.read().splitlines()

    map = np.array([list(line) for line in contraption])

    starts = [CellState((i,0), 'R') for i in range(map.shape[0])]
    starts += [CellState((map.shape[0]-1,j), 'U') for j in range(map.shape[1])]
    starts += [CellState((i,map.shape[1]-1), 'L') for i in range(map.shape[0])[::-1]]
    starts += [CellState((0,j), 'D') for j in range(map.shape[1])[::-1]]

    memoization = {}
    energized_cells = [propagate(s, map, memoization) for s in starts]

    toc = time.time()
    print('max number of energized cells:', max(energized_cells))
    print('time:', toc-tic)
