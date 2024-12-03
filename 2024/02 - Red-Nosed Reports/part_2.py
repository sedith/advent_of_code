import time
import math

sign = lambda x: math.copysign(1, x)


def check_levels_rec(report, dampener_used):
    crease = None
    for i, (level_0, level_1) in enumerate(zip(report[:-1], report[1:])):
        diff = level_1 - level_0
        if crease is None:
            crease = sign(diff)
        if diff == 0 or abs(diff) > 3 or sign(diff) != crease:
            if dampener_used:
                return False
            elif i == 1:
                return check_levels_rec(report[:i] + report[i+1:], True) \
                    or check_levels_rec(report[:i+1] + report[i+2:], True) \
                    or check_levels_rec(report[1:], True)
            elif diff == 0:
                return check_levels_rec(report[:i+1] + report[i+2:], True)
            else:
                return check_levels_rec(report[:i] + report[i+1:], True) \
                    or check_levels_rec(report[:i+1] + report[i+2:], True)
    return True


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
    reports = [list(map(int, report.split())) for report in input]

    safe = 0
    for report in reports:
        safe += check_levels_rec(report, False)

    toc = time.time()
    print('nb of safe reports:', safe)
    print('time:', toc-tic)
