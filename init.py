import os
import sys


template = \
"""


def main(data):
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


if __name__ == '__main__':
    folder = f'{sys.argv[1]}/{int(sys.argv[2]):02d} - {sys.argv[3]}'
    os.makedirs(folder)

    open(f'{folder}/input.txt', 'w')
    open(f'{folder}/example.txt', 'w')
    open(f'{folder}/README.md', 'w')
    open(f'{folder}/part2.py', 'w')
    with open(f'{folder}/part1.py', 'w') as f:
        f.write(template)
