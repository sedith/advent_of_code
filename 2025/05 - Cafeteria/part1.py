def main(data):
    blank_line = data.index('')
    ranges = [range(a, b+1) for a,b in map(lambda r: map(int, r.split('-')), data[:blank_line])]
    ingredients = map(int, data[blank_line + 1:])

    return sum(any(i in r for r in ranges) for i in ingredients)


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
