import numpy as np
import matplotlib.pyplot as plt
import time
from copy import copy


MOVES = {'U': np.array([0,-1]), 'D': np.array([0,1]), 'L': np.array([-1,0]), 'R': np.array([1,0])}
REFLECT_SLASH = {'U': 'R', 'L': 'D', 'D': 'L', 'R': 'U'}  # for / tiles
REFLECT_BACKSLASH = {'U': 'L', 'R': 'D', 'D': 'R', 'L': 'U'}  # for \ tiles

def check_ray(ray, map_contraption):
    rays = [ray]
    map_history = np.zeros_like(map_contraption)
    while len(rays):
        ## energize cells
        i = 0
        while i < len(rays):
            ray = rays[i]

            ## depop ray if it hits a wall or if it goes through a cell which have already been visited with the same direction (to avoid loops)
            if ray['cell'][0] < 0 or ray['cell'][0] >= map_contraption.shape[1] \
            or ray['cell'][1] < 0 or ray['cell'][1] >= map_contraption.shape[0] \
            or ray['dir'] in map_history[tuple(ray['cell'][::-1])]:
                del rays[i]
                break
            else:
                map_history[tuple(ray['cell'][::-1])] += ray['dir']

            ## propagate ray
            cell = map_contraption[tuple(ray['cell'][::-1])]
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
                    rays = [{'cell': copy(ray['cell']), 'dir': 'L'},  {'cell': copy(ray['cell']), 'dir': 'R'}] + rays
                    rays[0]['cell'] += MOVES[rays[0]['dir']]
                    rays[1]['cell'] += MOVES[rays[1]['dir']]
                    i += 2
                    del rays[i]
            elif cell == '|':
                if ray['dir'] == 'U' or ray['dir'] == 'D':
                    rays[i]['cell'] += MOVES[ray['dir']]
                    i += 1
                else:
                    rays = [{'cell': copy(ray['cell']), 'dir': 'D'},  {'cell': copy(ray['cell']), 'dir': 'U'}] + rays
                    rays[0]['cell'] += MOVES[rays[0]['dir']]
                    rays[1]['cell'] += MOVES[rays[1]['dir']]
                    i += 2
                    del rays[i]
            else:
                print('you should not be here!')

    map_energy = map_history != ''
    return np.count_nonzero(map_energy), map_energy


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        contraption_text = f.readlines()

    map_contraption = np.array([list(line[:-1]) for line in contraption_text])

    ## create all possible starting cells
    shape = map_contraption.shape
    starting_rays = []
    starting_rays += [{'cell': [0,i], 'dir': 'R'} for i in range(shape[0])]
    starting_rays += [{'cell': [shape[1]-1,i], 'dir': 'L'} for i in range(shape[0])]
    starting_rays += [{'cell': [i,0], 'dir': 'D'} for i in range(shape[1])]
    starting_rays += [{'cell': [i,shape[0]-1], 'dir': 'U'} for i in range(shape[1])]

    ## get max
    max_energy = 0
    map_max = None
    for i, starting_ray in enumerate(starting_rays):
        nb_cell_energized, map_energy = check_ray(starting_ray, map_contraption)

        if nb_cell_energized > max_energy:
            max_energy = nb_cell_energized
            map_max = map_energy

        print(i+1,'/',len(starting_rays),':',max_energy, end='\r')
    print()

    toc = time.time()
    print('max number of energized cells:', max_energy)
    print('time:', toc-tic)

    plt.imshow(map_max)
    plt.show()
