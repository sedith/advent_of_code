import time
import math

sign = lambda x: math.copysign(1, x)


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
    reports = [list(map(int, report.split())) for report in input]

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

    toc = time.time()
    print('nb of safe reports:', safe)
    print('time:', toc-tic)
