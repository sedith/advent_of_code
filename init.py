#!/usr/bin/env python3
import os
import sys


template_python = \
"""def main(data):
    return 0


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
"""

template_readme = \
"""# Advent of code %s - Day %s: %s

## Part 1



## Part 2
"""


if __name__ == '__main__':
    if len(sys.argv) >= 4:
        year, day, title = sys.argv[1], f'{int(sys.argv[2]):02d}', sys.argv[3]
        folder = f'{year}/{day} - {title}'
        os.makedirs(folder)

        open(f'{folder}/input.txt', 'w')
        open(f'{folder}/example.txt', 'w')
        open(f'{folder}/part2.py', 'w')
        with open(f'{folder}/part1.py', 'w') as f:
            f.write(template_python)
        with open(f'{folder}/README.md', 'w') as f:
            f.write(template_readme % (year, day, title))
