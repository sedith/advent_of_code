import re


def main(data):
    sum_mult = 0
    for line in data:
        nums = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
        while (match := nums.search(line)) is not None:
            match_str = match.group(0)
            n1, n2 = match_str[4:-1].split(',')
            sum_mult += int(n1) * int(n2)
            line = line[match.start() + len(match_str) :]

    return sum_mult


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
