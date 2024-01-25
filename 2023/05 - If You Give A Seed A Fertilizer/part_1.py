import numpy as np
import time


def parse_almanac(almanac):
    seeds = [int(s) for s in almanac[0].split(': ')[1].split()]

    maps = []
    for line in almanac[1:]:
        if not line:
            continue
        if line.endswith('map:'):
            maps += [[]]
            continue
        dst, src, size = line.split()
        maps[-1].append({'dst': int(dst), 'src': int(src), 'len': int(size)})

    return seeds, maps


def apply_map(nb, map):
    for mapping in map:
        if nb in range(mapping['src'], mapping['src']+mapping['len']):
            return nb + mapping['dst'] - mapping['src']
    return nb


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        almanac = f.read().splitlines()

    seeds, maps = parse_almanac(almanac)

    closest_location = None
    for s in seeds:
        for map in maps:
            s = apply_map(s, map)
        if not closest_location: closest_location = s
        else: closest_location = min(closest_location, s)

    toc = time.time()
    print('closest location:', closest_location)
    print('time:', toc-tic)
