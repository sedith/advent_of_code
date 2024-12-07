import time
from collections import defaultdict


def check_update(rules, update):
    for i, page in enumerate(update):
        for prev in rules[page]:
            if prev not in update[:i] and prev in update[i:]:
                return False
    return True

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
        if check_update(rules, update):
            sum_of_mid += int(update[len(update) // 2])


    toc = time.time()
    print('sum of middle of valid updates:', sum_of_mid)
    print('time:', toc-tic)
