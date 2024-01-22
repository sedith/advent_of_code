import numpy as np
import time


def check_possibility(springs, conditions):
    i = 0
    group_id = 0
    group_nb = 0
    for i,sp in enumerate(springs):
        if springs[i] == '#':
            group_nb += 1
        if springs[i] != '#' or i == len(springs)-1:
            if group_nb > 0:
                if group_id == len(conditions) or group_nb != conditions[group_id]:
                    return False
                group_nb = 0
                group_id += 1
    if group_id != len(conditions):
        return False
    return True


def get_possibilities(springs):
    ## find indices of ?s in the list
    unknowns = []
    while (i := springs.find('?')) != -1:
        unknowns.append(i)
        springs = springs.replace('?', 'X', 1)

    possibilities = []
    springs = springs.replace('X', '.')
    possibilities.append(springs)

    for _ in range(2**len(unknowns)-1):
        flip = True  # the last bit is always flipped
        new_springs = list(springs)
        for u in unknowns[::-1]:
            if flip:
                new_springs[u] = '.' if springs[u] == '#' else '#'
            flip = flip and springs[u] == '#'  # flip is all bits to the right are 1s (#s)
        springs = new_springs
        possibilities.append(''.join(new_springs))

    return possibilities


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        records = f.read().splitlines()

    sum_counts = 0
    for row in records:
        springs, conditions = row.split()
        conditions = list(map(int,conditions.split(',')))

        for p in get_possibilities(springs):
            sum_counts += check_possibility(p, conditions)

    toc = time.time()
    print('sum of counts of arrangements:', sum_counts)
    print('time:', toc-tic)
