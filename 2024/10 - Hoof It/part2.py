from collections import defaultdict


class GraphNode:
    def __init__(self, p, z):
        self.p = p
        self.z = z
        self.prev = []
        self.next = []

def rating_rec(node):
    if node.z == 9:
        return 1
    return 0 + sum([rating_rec(n) for n in node.next])


def explore_rec(z_map, loc):
    for d in [-1j, 1, 1j, -1]:
        np = loc.p + d
        if z_map[np] == loc.z + 1:
            next_loc = GraphNode(np, loc.z + 1)
            next_loc.prev.append(loc)
            loc.next.append(next_loc)
            explore_rec(z_map, next_loc)
    return loc


def main(data):
    z_map = defaultdict(int) | {j + 1j * i: int(c) for i, l in enumerate(data) for j, c in enumerate(l) if c.isdigit()}
    trails = [explore_rec(z_map, GraphNode(p, 0)) for p in list(z_map) if z_map[p] == 0]
    return sum(map(rating_rec, trails))


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
