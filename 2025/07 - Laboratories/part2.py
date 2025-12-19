from functools import cache


@cache
def explore_timeline_rec(beam):
    if beam[0] == len(data) - 1:
        return 1
    if data[beam[0]][beam[1]] == '^':
        return \
            explore_timeline_rec((beam[0] + 1, beam[1] - 1)) + \
            explore_timeline_rec((beam[0] + 1, beam[1] + 1))
    else:
        return explore_timeline_rec((beam[0] + 1, beam[1]))


def main(data):
    (start,) = ((i, j) for i, l in enumerate(data) for j, c in enumerate(l) if c == 'S')

    return explore_timeline_rec(start)


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
