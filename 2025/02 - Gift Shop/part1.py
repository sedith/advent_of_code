def main(data):
    ranges = [tuple(map(int, r.split('-'))) for r in data[0].split(',')]

    sum_ids = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            s = str(i)
            if len(s) % 2 == 0:
                h1 = s[:len(s)//2]
                h2 = s[len(s)//2:]
                if h1 == h2:
                    sum_ids += i
    return sum_ids


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
