from collections import defaultdict


def diskmap_to_blocks(diskmap):
    file_idx = 0
    file = True
    blocks = []
    for c in map(int, diskmap):
        for k in range(c):
            blocks.append(str(file_idx) if file else '.')
        file_idx += file
        file = not file
    return blocks


def defrag(blocks):
    ## locate empty blocks
    # free = defaultdict(list)
    free_idx = []
    free_size = []
    curr_size = 0
    for i, b in enumerate(blocks):
        if b == '.':
            curr_size += 1
        elif curr_size:
            free_idx.append(i - curr_size)
            free_size.append(curr_size)
            curr_size = 0

    ## defrag
    idx = int(1e9)
    curr_size = 0
    for i, b in enumerate(blocks[::-1]):
        if b != idx and curr_size:
            j = 0
            while j < len(free_size) and free_size[j] < curr_size:
                j += 1
            if j < len(free_size) and (slot := free_idx[j]) < len(blocks) - i:
                slot = free_idx[j]
                blocks[slot : slot + curr_size] = blocks[-i:][:curr_size]
                if i - curr_size:
                    blocks[-i:] = ['.'] * curr_size + blocks[-i + curr_size :]
                else:
                    blocks[-i:] = ['.'] * curr_size
                free_size[j] -= curr_size
                free_idx[j] += curr_size
                if free_size[j] < 1:
                    del free_size[j], free_idx[j]
        if b == '.' or int(b) > int(idx):
            curr_size = 0
        elif b == idx:
            curr_size += 1
        else:
            idx = b
            curr_size = 1

    return blocks


def checksum(blocks):
    return sum([i * int(f) for i, f in enumerate(blocks) if f != '.'])


def main(data):
    return checksum(defrag(diskmap_to_blocks(data[0])))


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
