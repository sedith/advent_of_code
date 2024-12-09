def algo_HASH(string):
    h = 0
    for c in string:
        h = ((h + ord(c)) * 17) % 256
    return h


def main(data):
    sum_hash = 0
    for string in data.split(','):
        sum_hash += algo_HASH(string)

    return sum_hash


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example.txt'
    with open(file, 'r') as f:
        data = f.read()[:-1]
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
