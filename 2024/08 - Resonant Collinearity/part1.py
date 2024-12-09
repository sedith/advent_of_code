from collections import defaultdict


def node_in_grid(ij):
    global grid_size
    return ij[0] in range(grid_size[0]) and ij[1] in range(grid_size[1])


def compute_antinodes(p1, p2):
    di = p1[0] - p2[0]
    dj = p1[1] - p2[1]
    return (p1[0] + di, p1[1] + dj), (p2[0] - di, p2[1] - dj)


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
                    antinodes.update([n for n in compute_antinodes(ant1, ant2) if node_in_grid(n)])

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
