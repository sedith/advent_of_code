import time
import re


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()

    sum_mult = 0
    for line in input:
        nums = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
        while (match := nums.search(line)) is not None:
            match_str = match.group(0)
            n1, n2 = match_str[4:-1].split(',')
            sum_mult += int(n1) * int(n2)
            line = line[match.start() + len(match_str):]

    toc = time.time()
    print('sum:', sum_mult)
    print('time:', toc-tic)
