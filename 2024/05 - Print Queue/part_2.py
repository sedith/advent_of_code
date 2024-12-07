import time
from collections import defaultdict
from copy import copy


def check_update(rules, update):
    fixed = copy(update)
    i = 0
    while i < len(update):
        page = fixed[i]
        for prev in rules[page]:
            if prev not in fixed[:i]:
                try:
                    j = fixed[i:].index(prev)
                    modif = True
                    fixed[i] = prev
                    fixed[i+j] = page
                    i -= 1
                    break
                except ValueError:
                    pass
        i += 1
    return fixed

if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    ## build ordering dict
    rules = defaultdict(list)
    while (rule := input.pop(0)) != '':
        prev, next = rule.split('|')
        rules[next].append(prev)

    ## check update
    sum_of_mid = 0
    for l in input:
        update = l.split(',')
        if (fixed := check_update(rules, update)) != update:
            sum_of_mid += int(fixed[len(fixed) // 2])


    toc = time.time()
    print('sum of middle of fixed updates:', sum_of_mid)
    print('time:', toc-tic)
