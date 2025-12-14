def main_naive(data):
    ranges = [tuple(map(int, r.split('-'))) for r in data[0].split(',')]

    sum_ids = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            s = str(i)
            ls = len(s)
            for k in range(ls//2 + 1, 1, -1):
                if ls % k == 0:
                    ss = s[:k]
                    if ss * (ls // k) == s:
                        sum_ids += i
                        break
    return sum_ids


def main(data):
    ranges = [range(*map(int, r.split('-'))) for r in data[0].split(',')]
    ranges = sorted(ranges, key=lambda r: r.start)  # useless a priori but it speeds up the loop by some % for some reason
    max_int = ranges[-1].stop
    max_digits = len(str(max_int))

    invalid_ids = set()
    for length in range(2, max_digits + 1):  # number of digits in candidate
        for seq_length in range(1, length // 2 + 1):  # lenght of repeated sequence
            if length % seq_length != 0:
                continue
            repeats = length // seq_length
            
            start = 10**(seq_length - 1)
            end = 10**seq_length

            for seq in map(str, range(start, end)):
                candidate = int(seq * repeats)
                if candidate > max_int: break  # given how candidates are sampled, there are many above the max so quick check instead of looping over ranges
                for r in ranges:
                    if candidate in r:
                        invalid_ids.add(candidate)
                        break

    return sum(invalid_ids)


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
