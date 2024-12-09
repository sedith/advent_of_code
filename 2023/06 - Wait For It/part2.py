import numpy as np


def solve_quadratic_eq(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return None
    if d == 0:
        return -b * 0.5 / a
    if d > 0:
        sd = np.sqrt(d)
        sols = [0.5 * (-b - sd) / a, 0.5 * (-b + sd) / a]
        sols.sort()
        return sols


def main(data):
    T, D = int(data[0].split(':')[1]), int(data[1].split(':')[1])

    ## solve - x**2 + x*T - D = 0
    sols = solve_quadratic_eq(-1, T, -D)

    return int(np.floor(sols[1]) - np.ceil(sols[0]) + 1)


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read().replace(' ', '').splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
