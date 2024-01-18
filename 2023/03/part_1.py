import numpy as np
import time


def check_symbols(array, row, col):
    for i in range(max(row-1, 0), min(row+2, array.shape[0])):
        for j in range(max(col-1, 0), min(col+2, array.shape[1])):
            if not array[i,j].isdigit() and array[i,j] != '.':
                return True
    return False


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        schematic_text = f.read().splitlines()

    schematic = np.array([list(line) for line in schematic_text])

    sum_part_numbers = 0
    digits = ''
    is_part_number = False
    for i, line in enumerate(schematic):
        for j, cell in enumerate(line):
            if cell.isdigit():
                digits += cell
                if not is_part_number:
                    is_part_number = check_symbols(schematic, i, j)
            else:
                if is_part_number:
                    sum_part_numbers += int(digits)
                digits = ''
                is_part_number = False

    toc = time.time()
    print('sum of part numbers:', sum_part_numbers)
    print('time:', toc-tic)
