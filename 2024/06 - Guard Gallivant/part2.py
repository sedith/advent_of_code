from collections import defaultdict


# def display(obs, pos, path, future_path, new_obs):
#     global size
#     to_print = [['.' for j in range(size[1])] for i in range(size[0])]
#     for o in obs:
#         to_print[int(o.imag)][int(o.real)] = '#'
#
#     for p in path:
#         if path[p]:
#             to_print[int(p.imag)][int(p.real)] = '\033[32mx\033[0m'  # actual path in green
#     for p in future_path:
#         if future_path[p]:
#             to_print[int(p.imag)][int(p.real)] = f'\033[93mx\033[0m'  # hypothetical path in yellow
#     to_print[int(pos.imag)][int(pos.real)] = f'\033[31mo\033[0m'  # current guard position in red
#     to_print[int(new_obs.imag)][int(new_obs.real)] = '\033[31m#\033[0m'  # proposed obstruction in red
#     print(''.join(''.join(line) + '\n' for line in to_print))


def explore(obs, path, p, dir):
    future_path = defaultdict(complex)
    new_obs = p + dir
    dir *= 1j
    while 1:
        while in_grid(np := p + dir) and np != new_obs and np not in obs:
            future_path[p] = dir
            p = np
        if not in_grid(np):
            return False
        while (np := p + dir) == new_obs or np in obs:
            dir *= 1j
        if path[p] == dir or future_path[p] == dir:
            return True


def in_grid(p):
    global size
    return 0 <= p.imag < size[0] and 0 <= p.real < size[1]


def main(data):
    global size
    size = len(data), len(data[0])
    obs = {j + i * 1j for i, l in enumerate(data) for j, c in enumerate(l) if c == '#'}

    (p,) = (j + i * 1j for i, l in enumerate(data) for j, c in enumerate(l) if c == '^')  # find start
    dir = -1j  # starts facing north

    ## increment guard path
    path = defaultdict(complex)
    new_obs = []
    while in_grid(p):
        while (np := p + dir) in obs:
            dir *= 1j  # rotate 90° clockwise
        path[p] = dir
        if in_grid(np) and np not in new_obs and not path[np]:  # check if we can obstruct the next cell
            if explore(obs, path, p, dir):
                new_obs.append(np)
        p = np
    return len(new_obs)


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
    print(f'time [size] : {toc - tic:.5f}')
