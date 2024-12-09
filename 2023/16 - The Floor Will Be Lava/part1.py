import numpy as np
import matplotlib.pyplot as plt
from copy import copy


MOVES = {'U': np.array([-1, 0]), 'D': np.array([1, 0]), 'L': np.array([0, -1]), 'R': np.array([0, 1])}
REFLECT_SLASH = {'U': 'R', 'L': 'D', 'D': 'L', 'R': 'U'}  # for / tiles
REFLECT_BACKSLASH = {'U': 'L', 'R': 'D', 'D': 'R', 'L': 'U'}  # for \ tiles


def propagate(start_ray, map):
    map_history = np.zeros_like(map)
    rays = [start_ray]

    while len(rays):
        i = 0
        while i < len(rays):
            ray = rays[i]

            ## depop ray if it hits a wall or if it goes through a cell which have already been visited with the same direction (to avoid loops)
            if (
                ray['cell'][0] < 0
                or ray['cell'][0] >= map.shape[1]
                or ray['cell'][1] < 0
                or ray['cell'][1] >= map.shape[0]
                or ray['dir'] in map_history[tuple(ray['cell'])]
            ):
                del rays[i]
                break
            else:
                map_history[tuple(ray['cell'])] += ray['dir']

            ## propagate ray
            cell = map[tuple(ray['cell'])]
            if cell == '.':
                rays[i]['cell'] += MOVES[ray['dir']]
                i += 1
            elif cell == '\\':
                rays[i]['dir'] = REFLECT_BACKSLASH[ray['dir']]
                rays[i]['cell'] += MOVES[ray['dir']]
                i += 1
            elif cell == '/':
                rays[i]['dir'] = REFLECT_SLASH[ray['dir']]
                rays[i]['cell'] += MOVES[ray['dir']]
                i += 1
            elif cell == '-':
                if ray['dir'] == 'L' or ray['dir'] == 'R':
                    rays[i]['cell'] += MOVES[ray['dir']]
                    i += 1
                else:
                    rays = [{'cell': copy(ray['cell']), 'dir': 'L'}, {'cell': copy(ray['cell']), 'dir': 'R'}] + rays
                    rays[0]['cell'] += MOVES[rays[0]['dir']]
                    rays[1]['cell'] += MOVES[rays[1]['dir']]
                    i += 2
                    del rays[i]
            elif cell == '|':
                if ray['dir'] == 'U' or ray['dir'] == 'D':
                    rays[i]['cell'] += MOVES[ray['dir']]
                    i += 1
                else:
                    rays = [{'cell': copy(ray['cell']), 'dir': 'D'}, {'cell': copy(ray['cell']), 'dir': 'U'}] + rays
                    rays[0]['cell'] += MOVES[rays[0]['dir']]
                    rays[1]['cell'] += MOVES[rays[1]['dir']]
                    i += 2
                    del rays[i]
            else:
                print('you should not be here!')

    map_energy = map_history != ''
    return np.count_nonzero(map_energy), map_energy


def main(data):
    map = np.array([list(line) for line in data])

    starting_ray = {'cell': [0, 0], 'dir': 'R'}

    nb_cell_energized, map_energy = propagate(starting_ray, map)

    # plt.imshow(map_energy)
    # plt.show()

    return nb_cell_energized


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
