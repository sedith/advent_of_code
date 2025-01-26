def main(data):
    blocks = [i // 2 if not i % 2 else -1 for i, size in enumerate(map(int, data)) for k in range(size)]
    files = [b for b in blocks if b >= 0]
    return sum((blocks[i] if blocks[i] >= 0 else files.pop()) * i for i in range(len(files)))


if __name__ == '__main__':
    import sys
    import time

    tic = time.time()
    file = 'input.txt' if sys.argv[1:] else 'example2.txt'
    with open(file, 'r') as f:
        data = f.read()[:-1]
    result = main(data)
    toc = time.time()
    print(f'result   : {result}')
    print(f'time [s] : {toc - tic:.5f}')
