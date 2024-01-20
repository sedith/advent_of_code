import numpy as np
import time


def expand_space(space_map):
    ## expand empty lines
    i = 0  # not defined through enumerate since the since of the array expands within the for loop
    for row in space_map:
        if '#' not in row:
            space_map = np.insert(space_map, i, '.', axis=0)
            i += 1
        i += 1

    ## expand empty collumns
    j = 0
    for col in space_map.T:
        if '#' not in col:
            space_map = np.insert(space_map, j, '.', axis=1)
            j += 1
        j += 1

    return space_map


def find_galaxies(space_map):
    galaxies = []
    for i, row in enumerate(space_map):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxies.append(np.array([i,j]))
    return galaxies


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        image = f.read().splitlines()

    space_map = np.array([list(line) for line in image])
    space_map = expand_space(space_map)

    galaxies = find_galaxies(space_map)

    sum_lenghts = 0
    for i,g1 in enumerate(galaxies[:-1]):
        for g2 in galaxies[i+1:]:
            sum_lenghts += np.linalg.norm(g1-g2, ord=1)

    sum_lenghts = int(sum_lenghts)

    toc = time.time()
    print('sum of lenghts:', sum_lenghts)
    print('time:', toc-tic)
