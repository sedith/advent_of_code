from functools import cache


def main(data):
    devices = {l[:3]: l[4:].split() for l in data}

    @cache
    def path_rec(dev):
        if dev == 'out':
            return 1
        return sum([path_rec(d) for d in devices[dev]])

    return path_rec('you')


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
