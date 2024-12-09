def main(data):
    sum = 0
    for line in data:
        d = [None, None]
        line = line.replace('one', 'o1e')
        line = line.replace('two', 't2o')
        line = line.replace('three', 't3e')
        line = line.replace('four', 'f4r')
        line = line.replace('five', 'f5e')
        line = line.replace('six', 's6x')
        line = line.replace('seven', 's7n')
        line = line.replace('eight', 'e8t')
        line = line.replace('nine', 'n9e')
        for c in line:
            if c.isdigit():
                if d[0] is None:
                    d[0] = int(c)
                else:
                    d[1] = int(c)
        if d[1] is None:
            d[1] = d[0]
        sum += 10 * d[0] + d[1]

    return sum


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
