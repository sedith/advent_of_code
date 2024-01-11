import numpy as np
import time


def solve_quadratic_eq(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    if d == 0:
        return -b * 0.5 / a
    if d > 0:
        sd = np.sqrt(d)
        sols = [0.5*(-b-sd)/a, 0.5*(-b+sd)/a]
        sols.sort()
        return sols

if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        sheet = f.read().replace(' ', '').splitlines()

    T, D = int(sheet[0].split(':')[1]), int(sheet[1].split(':')[1])

    ## solve - x**2 + x*T -d = 0
    sols = solve_quadratic_eq(-1, T, -D)

    ways_to_beat = int(np.floor(sols[1]) - np.ceil(sols[0]) + 1)

    toc = time.time()
    print('number of ways to beat record:', ways_to_beat)
    print('time:', toc-tic)
