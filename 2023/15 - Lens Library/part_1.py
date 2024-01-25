import numpy as np
import time


def algo_HASH(string):
    h = 0
    for c in string:
        h = ((h+ord(c)) * 17) % 256
    return h


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        sequence = f.read()[:-1]

    sum_hash = 0
    for string in sequence.split(','):
        sum_hash += algo_HASH(string)

    toc = time.time()
    print('sum of hashes:', sum_hash)
    print('time:', toc-tic)
