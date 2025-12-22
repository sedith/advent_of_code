def area(p1p2):
    p1 = p1p2[0] ; p2 = p1p2[1]
    return (abs(p1[0] - p2[0]) + 1 ) * (abs(p1[1] - p2[1]) + 1)


def main(data):
    points = [tuple(map(int, l.split(','))) for l in data]
    return area(max(((p1, p2) for i1, p1 in enumerate(points) for i2, p2 in enumerate(points) if i1 < i2), key=area))


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
