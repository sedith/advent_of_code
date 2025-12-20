def dist2(p1: list[int], p2: list[int]):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2


def main(data):
    points = [tuple(map(int, p.split(','))) for p in data]
    distances = {(p1, p2): dist2(p1, p2) for i1, p1 in enumerate(points) for i2, p2 in enumerate(points) if i1 < i2}
    pairs_sorted = sorted(distances.keys(), key=distances.get)

    circuits = [set(pairs_sorted[0])]
    for p1, p2 in pairs_sorted[1:]:
        nc = set([p1, p2])
        to_remove = []
        for i, c in enumerate(circuits):
            if p1 in c or p2 in c:
                nc.update(c)
                to_remove.append(i)
        for i in reversed(to_remove):
            del circuits[i]
        circuits.append(nc)

        if len(circuits) == 1 and len(circuits[0]) == len(points):
            break
    return p1[0] * p2[0]


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
