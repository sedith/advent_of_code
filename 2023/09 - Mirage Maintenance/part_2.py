import numpy as np
import time


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        readings = f.read().splitlines()

    reports = np.array([list(map(int,line.split())) for line in readings])

    sum_extrapolated = 0
    for line in reports:
        ## create successive sequences of differences
        diff = [line]
        while not all(diff[-1] == 0):
            diff.append(np.array([diff[-1][i+1]-diff[-1][i] for i in range(len(diff[-1])-1)]))

        ## regularization step: if the last diff sequence is empty (only one element left), add a 0 instead
        if not len(diff[-1]):
            diff[-1] = [0]

        ## go back and extrapolate each sequence until initial line
        extrapolated_val = 0
        for sequence in diff[::-1]:
            extrapolated_val = sequence[0] - extrapolated_val
        sum_extrapolated += extrapolated_val

    toc = time.time()
    print('sum of extrapolated values:', sum_extrapolated)
    print('time:', toc-tic)
