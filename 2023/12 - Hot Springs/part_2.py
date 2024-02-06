import numpy as np
import time
from copy import copy


def recursive_nb_valid(springs, conditions, idx_spring, idx_cond, size_block):
    key = (idx_spring, idx_cond, size_block)

    ## check memoization
    if key in memoization:
        return memoization[key]

    ## terminal conditions:
    ## the path is valid if the last spring has been scanned and:
    ## * the last block was already found
    ## * or the last spring is the last element of the last block
    if idx_spring == len(springs):
        if (idx_cond == len(conditions) and size_block == 0) \
        or (idx_cond == len(conditions)-1 and size_block == conditions[-1]):
            return 1
        else:
            return 0

    ## recursion
    rec_value = 0

    ## when scanning a '#', increment the size_block and go to next spring
    if springs[idx_spring] == '#':
        if idx_cond < len(conditions) and size_block < conditions[idx_cond]:
            rec_value += recursive_nb_valid(springs, conditions, idx_spring+1, idx_cond, size_block+1)
        else:
            return 0

    ## when scanning a '.', there are two cases:
    ## * if it does not terminates a block, go to next spring
    ## * else, increment the condition index, reset size_block and go to next spring
    elif springs[idx_spring] == '.':
        if size_block == 0:
            rec_value += recursive_nb_valid(springs, conditions, idx_spring+1, idx_cond, 0)
        elif idx_cond < len(conditions) and conditions[idx_cond] == size_block:
            rec_value += recursive_nb_valid(springs, conditions, idx_spring+1, idx_cond+1, 0)
        else:
            return 0

    ## when scanning a '?', query both possibilities
    else:
        if idx_cond < len(conditions) and size_block < conditions[idx_cond]:
            case1 = copy(springs)
            case1[idx_spring] = '#'
            rec_value += recursive_nb_valid(case1, conditions, idx_spring+1, idx_cond, size_block+1)

        case2 = copy(springs)
        case2[idx_spring] = '.'
        if size_block == 0:
            rec_value += recursive_nb_valid(case2, conditions, idx_spring+1, idx_cond, 0)
        elif idx_cond < len(conditions) and conditions[idx_cond] == size_block:
            rec_value += recursive_nb_valid(case2, conditions, idx_spring+1, idx_cond+1, 0)

    memoization[key] = rec_value
    return rec_value


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        records = f.read().splitlines()

    unfold_factor = 5  # number of copies of the initial list

    sum_counts = 0
    for row in records:
        springs, conditions = row.split()
        springs = list(springs)
        conditions = list(map(int,conditions.split(',')))

        # unfold lists
        ns = [] + springs ; nc = [] + conditions
        for _ in range(unfold_factor-1):
            ns += ['?'] + springs
            nc += conditions
        springs = ns ; conditions = nc

        global memoization
        memoization = {}  # memoization dict for dynamic programming
        sum_counts += recursive_nb_valid(springs, conditions, 0, 0, 0)

    toc = time.time()
    print('sum of counts of arrangements:', sum_counts)
    print('time:', toc-tic)
