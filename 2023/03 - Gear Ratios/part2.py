import numpy as np


def check_gear(array, row, col):
    for i in range(max(row - 1, 0), min(row + 2, array.shape[0])):
        for j in range(max(col - 1, 0), min(col + 2, array.shape[1])):
            if array[i, j] == '*':
                return (i, j)


def main(data):
    schematic = np.array([list(line) for line in data])

    gears = {}
    digits = ''
    gear = None
    for i, line in enumerate(schematic):
        for j, cell in enumerate(line):
            if cell.isdigit():
                digits += cell
                if not gear:
                    gear = check_gear(schematic, i, j)
            else:
                if gear:
                    if gear in gears.keys():
                        gears[gear].append(int(digits))
                    else:
                        gears[gear] = [int(digits)]
                digits = ''
                gear = None

    sum_gears = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            sum_gears += gears[gear][0] * gears[gear][1]

    return sum_gears


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
