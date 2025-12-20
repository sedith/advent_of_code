import numpy as np
import time
from enum import IntEnum
from typing import NamedTuple


class Dir(IntEnum):
    U = 0
    R = 1
    D = 2
    L = 3

    @staticmethod
    def cw(dir):
        return Dir((dir + 1) % 4)

    @staticmethod
    def ccw(dir):
        return Dir((dir - 1) % 4)


def add(t1, t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


def is_in_grid(ij, grid_shape):
    return ij[0] >= 0 and ij[0] < grid_shape[0] and ij[1] >= 0 and ij[1] < grid_shape[1]


MOVES = {Dir.U: (-1,0), Dir.D: (1,0), Dir.L: (0,-1), Dir.R: (0,1)}
def move(ij, dir):
    return add(ij, MOVES[dir])


class NodeID(NamedTuple):
    ij: tuple[int,int] = (0,0)
    dirs: tuple = ()

class Node(NamedTuple):
    id: NodeID
    length: int = 0
    path: list[tuple[int,int]] = []


def find_min(start_cell, grid):
    distances = {start_cell: 0}
    nodes = [start_cell]

    while nodes:
        node = nodes.pop()

        if node.id in distances and node.length > distances[node.id]['dist']:
            continue

        ## get neighbors
        if (node.id == start_cell):  # first node
            possible_dirs = [Dir.R, Dir.D]
        else:
            latest_dir = node.id.dirs[-1]
            possible_dirs = [Dir.cw(latest_dir), Dir.ccw(latest_dir)]
            # print(node.id.dirs, latest_dir)
            if len(node.id.dirs) < 3 or any(d != node.id.dirs[-1] for d in node.id.dirs[-3:]):
                possible_dirs.append(latest_dir)
            # possible_dirs.append(latest_dir)

        neighbors = []
        for d in possible_dirs:
            new_ij = move(node.id.ij, d)
            if is_in_grid(new_ij, grid.shape):
                if len(node.id.dirs) < 3:
                    dirs = node.id.dirs + (d,)
                else:
                    dirs = node.id.dirs[:-1] + (d,)
                neighbors.append(Node(NodeID(new_ij, dirs), node.length + grid[new_ij], node.path + [new_ij]))

        for n in neighbors:
            if n.id not in distances or n.length < distances[n.id]['dist']:
                distances[n.id] = {'dist': n.length, 'path': n.path}
            nodes.append(n)

    return distances



if __name__ == '__main__':
    tic = time.time()

    with open('example.txt', 'r') as f:
        city_map = f.read().splitlines()

    heat_loss_map = np.array([list(map(int, line)) for line in city_map])

    # G = {(i,j): int(c) for i,r in enumerate(open('input.txt')) for j,c in enumerate(r.strip())}
    distances = find_min((0,0), heat_loss_map)

    ij_end = add(heat_loss_map.shape, (-1,-1))
    # ij_end = (1,8)

    min_dist = 1e6
    min_path = None
    for k in distances:
        if k.ij == ij_end and distances[k]['dist'] < min_dist:
            min_dist = distances[k]['dist']
            min_path = distances[k]['path']

    print_heat_loss_map = [list(map(str,l)) for l in heat_loss_map]
    for ij in min_path:
        print_heat_loss_map[ij[0]][ij[1]] = f'\033[93m{heat_loss_map[ij]}\033[0m'
    print_heat_loss_map[ij[0]][ij[1]] = f'\033[91m{heat_loss_map[ij]}\033[0m'
    print(''.join([''.join(map(str,line))+'\n' for line in print_heat_loss_map]))

    toc = time.time()
    print('minimum heat loss:', min_dist)
    print('time:', toc-tic)
