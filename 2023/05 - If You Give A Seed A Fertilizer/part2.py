from math import sqrt


def parse_almanac(almanac):
    seeds_raw = [int(s) for s in almanac[0].split(': ')[1].split()]
    it = iter(seeds_raw)
    seeds = []
    for range_start in it:
        seeds += [range(range_start, range_start + next(it))]
    seeds.sort(key=lambda r: r[0])

    maps = []
    for line in almanac[1:]:
        if not line:
            continue
        if line.endswith('map:'):
            maps += [[]]
            continue
        dst, src, size = line.split()
        maps[-1].append({'dst': int(dst), 'src': int(src), 'len': int(size)})

    for map in maps:
        map.sort(key=lambda m: m['dst'])

    return seeds, maps


def count_seeds(seeds):
    nb_seeds = 0
    for seed_range in seeds:
        nb_seeds += len(seed_range)
    return nb_seeds


def is_valid_seed(s, seeds):
    for seed_range in seeds:
        if s in seed_range:
            return True
    return False


def is_valid_loc(loc, maps, seeds):
    s = loc
    for map in maps[::-1]:
        s = invert_map(s, map)
    return is_valid_seed(s, seeds)


def apply_map(nb, map):
    for mapping in map:
        if nb in range(mapping['src'], mapping['src'] + mapping['len']):
            return nb + mapping['dst'] - mapping['src']
    return nb


def invert_map(nb, map):
    for mapping in map:
        if nb in range(mapping['dst'], mapping['dst'] + mapping['len']):
            return nb + mapping['src'] - mapping['dst']
    return nb


def main(data):
    seeds, maps = parse_almanac(data)

    nb_seeds = count_seeds(seeds)
    print('nb_seeds :', nb_seeds)

    max_loc = maps[-1][-1]['dst'] + maps[-1][-1]['len']

    closest_location = None

    step = int(sqrt(max_loc))  # completely adhoc, it has to be small but big but smaller than max_loc
    loc = 0
    while not is_valid_loc(loc, maps, seeds):
        while step != 1 and is_valid_loc(loc + step, maps, seeds):
            step = max(int(step / 2), 1)
        loc += step

    return loc


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
