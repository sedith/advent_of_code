import numpy as np
import time


def algo_HASH(label):
    h = 0
    for c in label:
        h = ((h+ord(c)) * 17) % 256
    return h


if __name__ == '__main__':
    tic = time.time()

    with open('input.txt', 'r') as f:
        sequence = f.read()[:-1]

    boxes = [[] for _ in range(256)]

    sum_hash = 0
    for string in sequence.split(','):
        remove = not string[-1].isdigit()
        if remove:
            label = string[:-1]
        else:
            label = string[:-2]
            focal = string[-1]

        box_id = algo_HASH(label)

        idx = [i for i,(l,f) in enumerate(boxes[box_id]) if l == label]
        if remove:
            for i in idx: del boxes[box_id][i]
        else:
            if idx:
                for i in idx: boxes[box_id][i] = (label, focal)
            else:
                boxes[box_id].append((label, focal))

        # if len(idx) > 1:
        #     print(f'\nAfter "{string}"')
        #     for i, b in enumerate(boxes):
        #         if b:
        #             print(f'Box {i}: {b}')
        #     break

    focusing_power = 0
    for i, b in enumerate(boxes):
        for j,(l,f) in enumerate(b):
            focusing_power += (i+1) * (j+1) * int(f)

    toc = time.time()
    print('focusing power:', focusing_power)
    print('time:', toc-tic)
