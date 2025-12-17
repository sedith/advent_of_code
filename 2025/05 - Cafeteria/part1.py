def main(data):
    blank_line = data.index('')
    fresh_ids = [range(a, b+1) for a,b in map(lambda r: map(int, r.split('-')), data[:blank_line])]
    ingredients = map(int, data[blank_line + 1:])

    count_valid = 0
    for i in ingredients:
        for r in fresh_ids:
            if i in r:
                count_valid += 1
                break
    return count_valid


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
