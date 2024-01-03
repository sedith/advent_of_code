import numpy as np
import time


def check_symbols(area):
    for cell in area.flatten():
        if not cell.isdigit() and cell != '.':
            return True
    return False


def get_neighbors(array, row, col):
    return array[max(row-1, 0):min(row+2, array.shape[0]), max(col-1, 0):min(col+2, array.shape[1])]


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        schematic_text = f.readlines()

    schematic = np.array([list(line[:-1]) for line in schematic_text])

    sum_part_numbers = 0
    for j, line in enumerate(schematic):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits = line[i]
                is_part_number = check_symbols(get_neighbors(schematic, j, i))
                i += 1
                while i < len(line) and line[i].isdigit():
                    digits += line[i]
                    is_part_number = is_part_number or check_symbols(get_neighbors(schematic, j, i))
                    i += 1
                number = int(digits)
                if is_part_number:
                    sum_part_numbers += number
            else:
                i += 1

    toc = time.time()
    print('sum of part numbers:', sum_part_numbers)
    print('time:', toc-tic)
