def main(data):
    dial = 50
    nb_0 = 0
    for line in data:
        direction, distance = (1 if line[0] == 'R' else -1, int(line[1:]))
        dial = (dial + direction * distance) % 100
        if dial == 0:
            nb_0 += 1
    return nb_0


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
