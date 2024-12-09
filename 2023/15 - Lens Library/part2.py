def algo_HASH(label):
    h = 0
    for c in label:
        h = ((h + ord(c)) * 17) % 256
    return h


def main(data):
    boxes = [[] for _ in range(256)]

    sum_hash = 0
    for string in data.split(','):
        remove = not string[-1].isdigit()
        if remove:
            label = string[:-1]
        else:
            label = string[:-2]
            focal = string[-1]

        box_id = algo_HASH(label)

        idx = [i for i, (l, f) in enumerate(boxes[box_id]) if l == label]
        if remove:
            for i in idx:
                del boxes[box_id][i]
        else:
            if idx:
                for i in idx:
                    boxes[box_id][i] = (label, focal)
            else:
                boxes[box_id].append((label, focal))

    focusing_power = 0
    for i, b in enumerate(boxes):
        for j, (l, f) in enumerate(b):
            focusing_power += (i + 1) * (j + 1) * int(f)

    return focusing_power


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read()[:-1]
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
