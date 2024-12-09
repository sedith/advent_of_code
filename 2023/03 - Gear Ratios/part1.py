import numpy as np


def check_symbols(array, row, col):
    for i in range(max(row - 1, 0), min(row + 2, array.shape[0])):
        for j in range(max(col - 1, 0), min(col + 2, array.shape[1])):
            if not array[i, j].isdigit() and array[i, j] != '.':
                return True
    return False


def main(data):
    schematic = np.array([list(line) for line in data])

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

    return sum_part_numbers


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
