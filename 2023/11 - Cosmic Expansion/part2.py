import numpy as np


def expand_space(space_map, expand_factor):
    r, c = np.indices(space_map.shape)
    coordinate_map = np.array([(i, j) for i, j in zip(r.flatten(), c.flatten())]).reshape((space_map.shape[0], space_map.shape[1], 2))

    ## expand empty lines
    for i, row in enumerate(space_map):
        if '#' not in row:
            coordinate_map[i:, :, 0] += expand_factor - 1  # -1 because the row is already there once

    ## expand empty collumns
    for j, col in enumerate(space_map.T):
        if '#' not in col:
            coordinate_map[:, j:, 1] += expand_factor - 1

    return coordinate_map


def find_galaxies(space_map, coordinate_map):
    galaxies = []
    for i, row in enumerate(space_map):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxies.append(coordinate_map[i, j])
    return galaxies


def main(data):
    expand_factor = int(1e6)

    space_map = np.array([list(line) for line in data])
    coordinate_map = expand_space(space_map, expand_factor)
    galaxies = find_galaxies(space_map, coordinate_map)

    sum_lenghts = 0
    for i, g1 in enumerate(galaxies[:-1]):
        for g2 in galaxies[i + 1 :]:
            sum_lenghts += np.linalg.norm(g1 - g2, ord=1)

    return int(sum_lenghts)


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
