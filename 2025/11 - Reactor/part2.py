from functools import cache


def main(data):
    devices = {l[:3]: l[4:].split() for l in data}

    @cache
    def path_rec(valid, dev):
        if dev == 'out':
            return valid == 0b11
        return sum([path_rec(valid | (dev == 'dac') | 2 * (dev == 'fft') , d) for d in devices[dev]])

    return path_rec(0, 'svr')


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read().splitlines()
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
