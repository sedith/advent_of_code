from collections import defaultdict


def dp_min_xor(target, operands):
    dp = defaultdict(lambda: float('inf'))
    dp[0] = 0
    for op in operands:
        for x, cost in list(dp.items()):
            dp[x ^ op] = min(dp[x ^ op], cost + 1)
    return dp[target]


def parse_machine(line):
    t_str, *b_str, _ = line.split()
    target = int(t_str[-2:0:-1].replace('.', '0').replace('#', '1'), 2)
    buttons = list(map(lambda x: sum(1<<i for i in x), map(lambda x: eval(x[:-1]+',)'), b_str)))
    
    return target, buttons


def main(data):
    return sum([dp_min_xor(*parse_machine(line)) for line in data])


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
