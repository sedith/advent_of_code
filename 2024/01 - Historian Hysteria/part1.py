def main(data):
    lists = map(lambda x: [int(n) for n in x.split()], data)
    lists = list(map(list, zip(*lists)))  # transpose
    l1 = sorted(lists[0])
    l2 = sorted(lists[1])

    return sum([abs(n1 - n2) for n1, n2 in zip(l1, l2)])


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
