from itertools import accumulate


def main(data):
    diskmap = list(map(int, data))
    segments = [x for x in zip(accumulate([0]+diskmap), diskmap)]
    files, spaces = segments[::2], segments[1::2]

    for i, (file_pos, file_size) in reversed(list(enumerate(files))):
        for j, (space_pos, space_size) in enumerate(spaces[:i]):
            if space_pos < file_pos and space_size >= file_size:
                files[i] = (space_pos, file_size)
                spaces[j] = (space_pos + file_size, space_size - file_size)
                break

    return sum(id * size * (size + 2 * pos - 1) // 2 for id, (pos, size) in enumerate(files))


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read()[:-1]
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
