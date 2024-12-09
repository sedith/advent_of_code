import math


sign = lambda x: math.copysign(1, x)


def main(data):
    reports = [list(map(int, report.split())) for report in data]

    safe = 0
    for report in reports:
        crease = None
        ok = True
        for level_0, level_1 in zip(report[:-1], report[1:]):
            diff = level_1 - level_0
            if crease is None:
                crease = sign(diff)
            if diff == 0 or abs(diff) > 3 or sign(diff) != crease:
                ok = False
                break
        safe += ok

    return safe


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
