import numpy as np


def main(data):
    reports = np.array([list(map(int, line.split())) for line in data])

    sum_extrapolated = 0
    for line in reports:
        ## create successive sequences of differences
        diff = [line]
        while not all(diff[-1] == 0):
            diff.append(np.array([diff[-1][i + 1] - diff[-1][i] for i in range(len(diff[-1]) - 1)]))

        ## regularization step: if the last diff sequence is empty (only one element left), add a 0 instead
        if not len(diff[-1]):
            diff[-1] = [0]

        ## go back and extrapolate each sequence until initial line
        for sequence in diff[::-1]:
            sum_extrapolated += sequence[-1]

    return sum_extrapolated


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
