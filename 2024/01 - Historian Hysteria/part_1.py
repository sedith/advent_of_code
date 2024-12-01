import time

if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        input = f.read().splitlines()
    lists = map(lambda x: [int(n) for n in x.split()], input)
    lists = list(map(list, zip(*lists)))  # transpose
    l1 = sorted(lists[0])
    l2 = sorted(lists[1])

    dist = sum([abs(n1 - n2) for n1, n2 in zip(l1, l2)])

    toc = time.time()
    print('total distance:', dist)
    print('time:', toc-tic)
