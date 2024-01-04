import numpy as np
import time


def check_gear(array, row, col):
    for i in range(max(row-1, 0), min(row+2, array.shape[0])):
        for j in range(max(col-1, 0), min(col+2, array.shape[1])):
            if array[i,j] == '*':
                return (i,j)


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        schematic_text = f.readlines()

    schematic = np.array([list(line[:-1]) for line in schematic_text])

    gears = {}
    digits = ''
    gear = None
    for i, line in enumerate(schematic):
        j = 0
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


    toc = time.time()
    print('sum of gear ratios:', sum_gears)
    print('time:', toc-tic)
