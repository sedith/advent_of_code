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
    i = 0
    j = len(blocks) - 1
    while 1:
        while blocks[i] != '.':
            i += 1
        while blocks[j] == '.':
            j -= 1
        if j > i:
            blocks[i] = blocks[j]
            blocks[j] = '.'
            i += 1
        else:
            break
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
