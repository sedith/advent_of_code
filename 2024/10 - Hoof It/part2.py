from enum import Enum


class Dir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def cw(self):
        return Dir((self.value + 1) % 4)

    def ccw(self):
        return Dir((self.value - 1) % 4)

    def move(self):
        return ((-1, 0), (0, 1), (1, 0), (0, -1))[self.value]

    def __str__(self):
        return ('^', '>', 'v', '<')[self.value]


class Pos(tuple):
    def __new__(cls, i, j, grid_size):
        return super(Pos, cls).__new__(cls, (i, j))

    def __init__(self, i, j, grid_size):
        self.grid_size = grid_size

    def __add__(self, d):
        di, dj = d.move()
        i = self[0] + di
        j = self[1] + dj
        if i in [-1, self.grid_size[0]] or j in [-1, self.grid_size[1]]:
            return None
        return Pos(i, j, self.grid_size)

    def next(self):
        if self[1] == self.grid_size[1] - 1:
            if self[0] == self.grid_size[0] - 1:
                return None
            else:
                return Pos(self[0] + 1, 0, self.grid_size)
        else:
            return Pos(self[0], self[1] + 1, self.grid_size)


class GraphNode:
    def __init__(self, pos, z):
        self.pos = pos
        self.z = z
        self.prev = []
        self.next = []


def get_z(pos):
    global z_map
    try:
        return int(z_map[pos[0]][pos[1]])
    except ValueError:
        return -1


def get_rating_rec(node):
    if node.z == 9:
        return 1
    return 0 + sum([get_rating_rec(n) for n in node.next])


def print_trail_rec(node):
    print(f'{node.pos} ({node.z}) -> {[n.pos for n in node.next]}')
    for n in node.next:
        print_trail_rec(n)


def main(data):
    grid_size = (len(data), len(data[0]))
    global z_map
    z_map = [[c for c in l] for l in data]

    trails = []
    cursor = Pos(0, 0, grid_size)
    while cursor is not None:
        if get_z(cursor) == 0:
            head = GraphNode(cursor, 0)
            trail = [head]
            while trail:
                loc = trail.pop()
                for d in [Dir.N, Dir.E, Dir.S, Dir.W]:
                    next_pos = loc.pos + d
                    if next_pos and get_z(next_pos) == loc.z + 1:
                        next_loc = GraphNode(next_pos, loc.z + 1)
                        next_loc.prev.append(loc)
                        loc.next.append(next_loc)
                        trail.append(next_loc)
            trails.append(head)
        cursor = cursor.next()

    return sum([get_rating_rec(t) for t in trails])


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example8.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
