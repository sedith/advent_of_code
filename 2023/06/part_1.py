import numpy as np
import time


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        sheet = f.read().splitlines()

    races = list(map(lambda t: (int(t[0]), int(t[1])), zip(sheet[0].split()[1:], sheet[1].split()[1:])))  # (so legible)

    solution = 1
    for T, D in races:
        ways_to_beat = 0
        cases = range(1,T)  # segment open to both ends since those are degenerate (0 travel distance)
        for press_T in cases:
            V = press_T
            if V * (T - press_T) > D:
                ways_to_beat += 1
        solution *= ways_to_beat

    toc = time.time()
    print('product of number of ways to beat records:', solution)
    print('time:', toc-tic)
