from collections import defaultdict


def node_in_grid(ij):
    global grid_size
    return ij[0] in range(grid_size[0]) and ij[1] in range(grid_size[1])


def compute_antinodes(p1, p2):
    nodes = [p1, p2]
    k = 1
    di = p1[0] - p2[0]
    dj = p1[1] - p2[1]
    n1_is_in = True
    n2_is_in = True
    while n1_is_in or n2_is_in:
        n1 = (p1[0] + k * di, p1[1] + k * dj)
        n1_is_in = node_in_grid(n1)
        if n1_is_in:
            nodes.append(n1)

        n2 = (p2[0] - k * di, p2[1] - k * dj)
        n2_is_in = node_in_grid(n2)
        if n2_is_in:
            nodes.append(n2)

        k += 1
    return nodes


def main(data):
    global grid_size
    grid_size = (len(data), len(data[0]))

    ## find list of antennas
    antennas = defaultdict(list)
    for i, l in enumerate(data):
        for j, c in enumerate(l):
            if c != '.':
                antennas[c].append((i, j))

    ## compute antinodes
    antinodes = set()
    for key in antennas:
        for ant1 in antennas[key]:
            for ant2 in antennas[key]:
                if ant1 != ant2:
                    antinodes.update(compute_antinodes(ant1, ant2))

    # ## display
    # grid = [[c for c in l] for l in data]
    # for ij in antinodes:
    #     if grid[ij[0]][ij[1]] == '.':
    #         grid[ij[0]][ij[1]] = '\033[32m#\033[0m'
    #     else:
    #         grid[ij[0]][ij[1]] = '\033[31m#\033[0m'
    # # for ij in antennas[key]:
    # #     grid[ij[0]][ij[1]] = f'\033[93m{key}\033[0m'
    # print(''.join(''.join(l) + '\n' for l in grid)[:-1])
    # # input()

    return len(antinodes)


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
