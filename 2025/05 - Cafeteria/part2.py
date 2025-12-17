def main(data):
    blank_line = data.index('')
    fresh_ids = sorted([range(a, b+1) for a,b in map(lambda r: map(int, r.split('-')), data[:blank_line])], key=lambda r: r.start)

    parsed_ranges = []
    for r1 in fresh_ids:
        merged = False
        for ir2, r2 in enumerate(parsed_ranges):
            if r1.start in r2 or r1.stop in r2:
                parsed_ranges[ir2] = range(r2.start, max(r1.stop, r2.stop))
                merge = True
                break
        if not merged:
            parsed_ranges.append(r1)
    return sum(len(r) for r in parsed_ranges)


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
