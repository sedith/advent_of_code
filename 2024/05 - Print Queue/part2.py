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
                    fixed[i + j] = page
                    i -= 1
                    break
                except ValueError:
                    pass
        i += 1
    return fixed


def main(data):
    ## build ordering dict
    rules = defaultdict(list)
    while (rule := data.pop(0)) != '':
        prev, next = rule.split('|')
        rules[next].append(prev)

    ## check update
    sum_of_mid = 0
    for l in data:
        update = l.split(',')
        if (fixed := check_update(rules, update)) != update:
            sum_of_mid += int(fixed[len(fixed) // 2])

    return sum_of_mid


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
