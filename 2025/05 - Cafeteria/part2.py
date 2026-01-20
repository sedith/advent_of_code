def main(data):
    blank_line = data.index('')
    ranges = sorted([range(a, b+1) for a,b in map(lambda r: map(int, r.split('-')), data[:blank_line])], key=lambda r: r.start)

    parsed_ranges = [ranges[0]]
    for r in ranges[1:]:
        if r.start <= parsed_ranges[-1].stop:
            parsed_ranges[-1] = range(parsed_ranges[-1].start, max(r.stop, parsed_ranges[-1].stop))
        else:
            parsed_ranges.append(r)
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
