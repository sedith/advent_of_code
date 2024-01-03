import time


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        instructions = f.readlines()

    sum = 0
    for line in instructions:
        d = [None,None]
        for c in line:
            if c.isdigit():
                if d[0] is None: d[0] = int(c)
                else: d[1] = int(c)
        if d[1] is None: d[1] = d[0]
        sum += 10*d[0] + d[1]

    toc = time.time()
    print('sum of instructions:', sum)
    print('time:', round(toc-tic, 4))
