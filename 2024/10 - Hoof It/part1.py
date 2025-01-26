from collections import defaultdict


def explore_rec(z_map, positions, level):
    if level == 10:
        return len(positions)

    new_pos = set(p + d for p in positions for d in [-1j, 1, 1j, -1] if z_map[p + d] == level)
    return explore_rec(z_map, new_pos, level + 1)


def main(data):
    z_map = defaultdict(int) | {j + 1j * i: int(c) for i, l in enumerate(data) for j, c in enumerate(l) if c.isdigit()}
    return sum(explore_rec(z_map, [p], 1) for p in list(z_map) if z_map[p] == 0)


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
