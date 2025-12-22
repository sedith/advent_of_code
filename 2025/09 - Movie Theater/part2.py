from itertools import pairwise, combinations


def area(p1p2):
    p1 = p1p2[0] ; p2 = p1p2[1]
    return (abs(p1[0] - p2[0]) + 1 ) * (abs(p1[1] - p2[1]) + 1)


def is_valid(rect, vertical_edges, horizontal_edges):
    (xmin, xmax), (ymin, ymax) = map(sorted, zip(*rect))
    for y, x1, x2 in vertical_edges:
        if (ymin < y < ymax and xmin < x2 and x1 < xmax):
            return False
    for x, y1, y2 in horizontal_edges:
        if xmin < x < xmax and ymin < y2 and y1 < ymax:
            return False
    return True


def main(data):
    points = [tuple(map(int, l.split(','))) for l in data]
    sorted_rectangles = sorted(combinations(points, 2), key=area, reverse=True)

    ## edges are stored (x, y1, y2) with y1 < y2 for horizontal ones (and accordingly for vertical ones)
    horizontal_edges = []
    vertical_edges = []
    for edge in pairwise(points + [points[0]]):
        if edge[0][0] == edge[1][0]:
            horizontal_edges.append([edge[0][0], *sorted([edge[0][1], edge[1][1]])])
        else:
            vertical_edges.append([edge[0][1], *sorted([edge[0][0], edge[1][0]])])

    for rect in sorted_rectangles:
        if is_valid(rect, vertical_edges, horizontal_edges):
            return area(rect)


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
