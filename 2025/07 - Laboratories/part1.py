def show(grid, trail):
    start = '\033[91mS\033[0m'
    beam = '\033[91m|\033[0m'
    splitter = '\033[91m^\033[0m'

    for line in trail:
        for b in line:
            if grid[b[0]][b[1]] == 'S':
                grid[b[0]][b[1]] = start
            elif grid[b[0]][b[1]] == '^':
                grid[b[0]][b[1]] = splitter
            else:
                grid[b[0]][b[1]] = beam

    print('\n'.join([''.join(line) for line in grid]))


def propagate_beam(pos):
    return (pos[0] + 1, pos[1])


split_count = 0
def split_beam(pos):
    global split_count
    split_count += 1
    return [(pos[0] + 1, pos[1] - 1), (pos[0] + 1, pos[1] + 1)]


def main(data):
    (start,) = ((i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == 'S')

    trail = [[start]]
    for i in range(len(data)-1):
        trail.append(set([propagate_beam(b) for b in trail[-1] if data[b[0]][b[1]] in ['.', 'S']] + [sb for b in trail[-1] if data[b[0]][b[1]] == '^' for sb in split_beam(b)]))
    show([list(s) for s in data], trail)
    return split_count


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
