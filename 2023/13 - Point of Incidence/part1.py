import numpy as np


def main(data):
    ## read patterns as individual np arrays
    patterns = []
    pattern = []
    for i, row in enumerate(data):
        if not row or i == len(data) - 1:
            patterns.append(np.array(pattern))
            pattern = []
        else:
            pattern.append(list(row))

    sum_reflexions = 0
    for pattern in patterns:
        ## first look for horizontal symmetry axis
        horz = 0
        for i in range(pattern.shape[0] - 1):
            if all(pattern[i, :] == pattern[i + 1, :]):
                k = 1
                global_symmetry = True
                while i - k >= 0 and i + k + 1 < pattern.shape[0]:
                    if not all(pattern[i - k, :] == pattern[i + k + 1, :]):
                        global_symmetry = False
                        break
                    k += 1
                if global_symmetry:
                    horz = i + 1
                    break

        ## if none found, look to vertical symmetry axis
        vert = 0
        if horz == 0:
            for j in range(pattern.shape[1] - 1):
                if all(pattern[:, j] == pattern[:, j + 1]):
                    k = 1
                    global_symmetry = True
                    while j - k >= 0 and j + k + 1 < pattern.shape[1]:
                        if not all(pattern[:, j - k] == pattern[:, j + k + 1]):
                            global_symmetry = False
                            break
                        k += 1
                    if global_symmetry:
                        vert = j + 1
                        break

        sum_reflexions += 100 * horz + vert

    return sum_reflexions


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
