from collections import defaultdict


def check_update(rules, update):
    for i, page in enumerate(update):
        for prev in rules[page]:
            if prev not in update[:i] and prev in update[i:]:
                return False
    return True


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
        if check_update(rules, update):
            sum_of_mid += int(update[len(update) // 2])

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
